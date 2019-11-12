import requests
import json
import auth

API_BASE_URL = "https://api.profootballfocus.com"

class ProFootballFocusAPI:
    
    def __init__(self, api_key=""):
        self.api_key = api_key
        self.jwt = None

    def get_token(self, api_key=None):
        """
        Gets and sets the JWT token necessary for making calls to the API. 
        """
        if api_key is None:
            api_key = self.api_key
        headers = {'x-api-key': api_key}
        resp = requests.post(API_BASE_URL + "/auth/login", headers=headers)
        if resp.status_code > 299:
            print("Authentication Failed.")
            self.jwt = None
        else:
            self.jwt = json.loads(resp.content)['jwt']
        print(self.jwt)

    def call_api(self, path, header=None):

        #we need a token before we can make an api call
        if self.jwt is None:
            self.get_token()
        
        if self.jwt is None:
            return -1, {}
        
        headers = {"Authorization": "Bearer " + self.jwt}
        if not header is None:
            for key, val in header.items():
                headers[key] = val
        resp = requests.get(API_BASE_URL + path, headers=headers)
        if resp.status_code > 299:
            print(resp.content)
            print("Call failed")
        
        return json.loads(resp.content)
        
        
        
    
