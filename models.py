from uuid import uuid4
from __init__ import bcrypt, mongo
from datetime import datetime
from flask import session

# the User class


class User:
    # initializing the class
    # def __init__(self, ):
    #     self.username = username
    #     self.email = email
    #     self.password = password

    # signup helper function
    @staticmethod
    def signup(fname=None, lname=None, email=None, password=None):

        try:
            user = {
                '_id': uuid4().hex,
                'fname': fname.lower(),
                'lname': lname.lower(),
                'email': email.lower(),
                'password': bcrypt.generate_password_hash(password).decode('utf-8'),
                'join_date': datetime.utcnow()
            }

            mongo.db.users.insert_one(user)
        except:
            return False

        return True

    # creating a user session
    @staticmethod
    def init_session(user):
        session['is_authenticated'] = True
        del user['password']
        session['current_user'] = user
        session.permanent = True
        return user

    # signin helper function
    def signin(self, form):

        # querying user from db  with email
        user = mongo.db.users.find_one(
            {"email": form['email'].lower()})

        # validating user and password
        if user and bcrypt.check_password_hash(user["password"], form['password']):
            return self.init_session(user)

        return False

    # signout helper function
    @staticmethod
    def signout():
        if session['is_authenticated'] and session['current_user']:
            session['is_authenticated'] = False
            del session['current_user']
        return True

    # get user by id
    @staticmethod
    def get(id):
        return mongo.db.users.find_one({'_id': id})

    # save scan data
    @staticmethod
    def save(id, data):
        data['author'] = id
        data['_id'] = uuid4().hex
        data['dateCreated'] = datetime.utcnow()
        mongo.db.scans.insert_one(data)
        return True

    # get all scan data
    @staticmethod
    def query(user):
        return mongo.db.scans.find({'author': user}).sort('dateCreated', -1)

    # fetch one scan data
    @staticmethod
    def fetch(id, user):
        return mongo.db.scans.find_one({'author': user, '_id': id})

    # save a new schedule
    @staticmethod
    def schedule(data):
        data['_id'] = uuid4().hex
        return mongo.db.schedule.insert_one(data)

    # getting the schedules
    @staticmethod
    def get_schedules(id):
        return mongo.db.schedule.find({'owner': id})

    # getting the schedules
    @staticmethod
    def unschedule(id):
        return mongo.db.schedule.delete_one({'_id': id})
