import requests

class Oauth(object):
    client_id = "671860130559688705" #client id id/code
    client_secret = "HryFwJ0RQawzGo31whWo5v_oaC3UHsGa" #client secret id/code
    scope = "identify%20email%20connections%20guilds%20guilds.join%20gdm.join%20rpc%20messages.read" #scopes from the application
    redirect_uri = "http://127.0.0.1:5000/login" #redirect uri 
    discord_login_url = "https://discordapp.com/api/oauth2/authorize?client_id={}&redirect_uri={}&response_type=code&scope={}".format(client_id, redirect_uri, scope) #discord login url
    discord_token_url = "https://discordapp.com/api/oauth2/token" #discord token url 
    discord_api_url = "https://discordapp.com/api" #discord api page

    @staticmethod
    def get_acccess_token(code):
        payload = { #all items in this dictionary are part of the required parameters in order to get the token url
            'client_id': Oauth.client_id,                       
            'client_secret': Oauth.client_secret, 
            'grant_type': "authorization_code",
            'code': code,
            'redirect_uri': Oauth.redirect_uri,
            'scope': Oauth.scope
        }
        
        headers = { #just a header
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = requests.post(url = Oauth.discord_token_url, data = payload, headers = headers) #gets the access token
        json = access_token.json()
        return json.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = Oauth.discord_api_url + "/users/@me"

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        user_object = requests.get(url = url, headers = headers)
        user_json = user_object.json()
        return user_json
