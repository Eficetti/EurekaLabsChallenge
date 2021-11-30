# EurekaLabsChallenge

Hi! First of all let me thank you for the opportunity to take this challenge!. It was a lot of fun,now we can start!

for using this API to see the stock market you are gonna need install the libs in requirements.txt
after those are install set the app with FLASK_APP=main.py and flask run

For create a USER use: 
http://127.0.0.1:5000/api/register 
and in the body add this Json structure :
{
    "email": "admin123@root123.com",
    "password": "admin",
    "name": "admin1234",
    "last_name": "root123"
}

For login into a user already register use:
http://127.0.0.1:5000/api/login
with this Json:
{
    "email": "admin123@root123.com",
    "password": "admin",
    "name": "admin1234",
    "last_name": "root123"
}
This call is gonna give u a token to use in the main part of this API

And for check the stock market use:
http://127.0.0.1:5000/api/stockMarket
with this body: 
{
    "Symbol": "FB" 
}
AND add the token previously received:
Bearer '%TOKEN%'

I was planning on using heroku to deploy but since im on a dead line, i dont have enought time for fixing errors. I know is not perfect but in looking forward to learn more!
A little feedback would do me good to improve! Greetings
