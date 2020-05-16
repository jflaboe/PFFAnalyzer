import os
import time
import requests
import sqlite3 # This may be upgraded to MySQL eventually
import csv
import sys


# When given an api-key, make a csv of all 2019 B1G games
# Providing game level detail
# string -> csv
def mainloop():
    
    key = os.environ['PFF_API_KEY']
    params = get_params(key)
    
    teams = get_teams(["NFC","AFC"], params)
    all_games = get_games(teams, params)

    DB_PATH = "pff.db"

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT MAX(updated_at_timestamp) FROM game")
    last_update_time = cursor.fetchall()[0][0]

    # only for the first run
    if (last_update_time is None):
        last_update_time = 0

    cursor.execute("SELECT id FROM game")
    dirty_existing_ids = cursor.fetchall()
    existing_ids = [id_num[0] for id_num in dirty_existing_ids]
    updated_game_ids = []
    for game in all_games:
        if game['updated_at_timestamp'] > last_update_time:
            if game['id'] in existing_ids:
                enter_data('update ' + str(game['id']), game, 'game', cursor)
            else:
                enter_data('insert', game, 'game', cursor)
            updated_game_ids.append(game['id'])

    print(updated_game_ids)
    connection.commit()
    connection.close()
    

# I should eventually use John's system
# Turn an api key into a jwt key and format as header
# str -> {str: str}
def get_params (key):
    params = {'x-api-key':key}
    r = requests.post('https://api.profootballfocus.com/auth/login', headers = params)
    jwt = r.json()['jwt']
    params = {'Authorization':'Bearer ' + jwt}
    return params

# Grab all team names that are part of a given group
# str, {str: str} -> listof str
def get_teams (names, params):
    teams = []
    r = requests.get('https://api.profootballfocus.com/v1/nfl/2019/teams', headers = params)
    for team in r.json()['teams']:
        for group in team['groups']:
            if group['name'] in names:
                teams.append(team['abbreviation'])

    return teams

# For B1G opponents, return all game ids in which they played in 2019
# And report the id first, then winning team, then the losing team
# str, {str: str} -> listof str
def get_games (opponents, params):
    r = requests.get('https://api.profootballfocus.com/v1/video/nfl/games', headers = params)

    games = []
    for game in r.json()['games']:
        if game['away_team'] in opponents and game['home_team'] in opponents:
            if game['season'] >= 2019:
                games.append(game)
    return games

def enter_data(op, data, table, cursor):
    keys = []
    values = []
    for key, value in data.items():
        if not value is None:
            keys.append(str(key))
            if isinstance(value, str):
                values.append("\"" + value + "\"")
            else:
                values.append(str(value))

    if op == 'insert':
        qstring = ('INSERT INTO ' + table + ' (' + ",".join(keys) + ')'
                   + ' VALUES (' + ",".join(values) + ');')
    elif op.split()[0] == 'update':
        qstring = ('UPDATE ' + table + ' SET (' + ",".join(keys) + ')'
                   + ' = (' + ",".join(values) + ')'
                   + ' WHERE id = ' + op.split()[1] + ';')

    print(qstring)
    cursor.execute(qstring)

mainloop()
