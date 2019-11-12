import pffapi
import sqlite3


api = pffapi.ProFootballFocusAPI(api_key = pffapi.auth.APIKEY)

def insert_game(game):
    connection = sqlite3.connect("pff.db")
    cursor = connection.cursor()
    keys = []
    values = []
    for key, value in game.items():
        if not value is None:
            keys.append(str(key))
            if isinstance(value, str):
                values.append("\"" + value + "\"")
            else:
                values.append(str(value))
    
    qstring = 'INSERT INTO game (' + ",".join(keys) + ') VALUES (' + ",".join(values) + ');'
    print(qstring)
    cursor.execute(qstring)
    connection.commit()
    connection.close()