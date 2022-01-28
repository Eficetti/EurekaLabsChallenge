# IMPORTS

from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from requests import get
from routes.auth import auth
from routes.stockMarket import market
from flask_jwt_extended import JWTManager, jwt_required
from db import db
import logSystem
    
# APP RUN AND  CONFIG 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'this-is-my-secret-key'
db.init_app(app)
jwt = JWTManager(app)
app.logger.info('Starting server...')

# API throttling is set to 10 calls per minute for the auth routes and 5 to the stocks because Alpha Vantage only accepts 5 per minute!

limiter = Limiter(app, key_func=get_remote_address)
limiter.limit("10/minute")(auth)
limiter.limit("5/minute")(market)

# BLUEPRINTS REGISTER 

app.register_blueprint(market, url_prefix='/api')
app.register_blueprint(auth, url_prefix='/api')


if __name__=='__main__':
    app.run(debug=True)

