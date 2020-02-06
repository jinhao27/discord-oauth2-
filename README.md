# discord-oauth2
This program utilizes flask in order to integrate Discord's oauth2 login API into a JA Company's website login. 

Using flask, along with some other libraries, this project assists with login authentication through Discord's oauth2 API. 
Through this, the program can obtain things related to various scopes from Discord, such as identity or email. From that, 
the program can obtain data and information such as user ID, username, email, and third party connections just to name a few. 
It's still a work in progress and is only connected locally through a flask environment. 

Some dependencies include flask, oauth2, Discord's API, as well as a few others. All are included at the top of the program. The 
oauth2 parts are written using classes, making it easily adjustable for various other Scopes that can be selected from the Discord 
Development API portal area. 
