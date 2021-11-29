from flask import Flask, request, blueprints
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from models import User
from db import db

# BLUEPRINT FOR AUTH #
auth = blueprints.Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
# get the user data from json to upload to the database #
def register():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        name = request.json.get('name', None)
        last_name = request.json.get('last_name', None)
        
        # check everything is on the json, if not raise a error  #
        if not email:
            return 'Missing email!', 400
        if not password:
            return 'Missing password!', 400
        if not name:
            return 'Missing name!', 400
        if not last_name:
            return 'Missing last name!', 400
        
        # Hash the password for more security #
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create the user to commit #
        user = User(email=email, name=name,last_name=last_name, hash=hashed)
        db.session.add(user)
        db.session.commit()

        # Create the access token for the user register via email because its unique #
        access_token = create_access_token(identity={"email": email})
        return {"access_token": access_token}, 200
    except IntegrityError:
        # the rollback function reverts the changes made to the db ( so if an error happens after we commited changes they will be reverted )
        db.session.rollback()
        return 'User Already Exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

# Gets the login information and validate if everything checks #
@auth.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        name = request.json.get('name', None)
        last_name = request.json.get('last_name', None)
        
        if not email:
            return 'Missing email!', 400
        if not password:
            return 'Missing password!', 400
        if not name:
            return 'Missing name!', 400
        if not last_name:
            return 'Missing last name!', 400


        user = User.query.filter_by(email=email).first()
        
        if not user:
            return 'User Not Found!', 404
        
        if bcrypt.checkpw(password.encode('utf-8'), user.hash):
            access_token = create_access_token(identity={"email": email})
            return {"access_token": access_token}, 200
        else:
            return 'Invalid Login Info!', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400
