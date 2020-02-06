from flask import Flask, request, render_template, redirect, session
from oauth import Oauth

app = Flask(__name__)

@app.route("/",methods = ["get"])
def index():
    return redirect(Oauth.discord_login_url) #redirects to the discord login confirmation page

@app.route("/login",methods = ["get"])
def login():
    code = request.args.get("code") 
    access_token = Oauth.get_acccess_token(code) 
    user_json = Oauth.get_user_json(access_token) 
    #somehow uses json to obtain the following information from the user's authorization 
    username = user_json.get("username") 
    identification = user_json.get("id") 
    user_tag = user_json.get("discriminator") 
    verified = user_json.get("verified") 
    email = user_json.get("email") 

    return email

if(__name__ == "__main__"):
    app.run(debug=True)

