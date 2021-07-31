from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from config import Config
from flask_cors import CORS
from flask_mail import Mail

# instantiating  pymongo
mongo = PyMongo()
# mongo = "make"

# instantiating bcrypt for password hash
bcrypt = Bcrypt()

# instantiating mail for sending emails
Mail = Mail()

# setting up CORS
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    Mail.init_app(app)

    from routes import main
    app.register_blueprint(main)
    # from abbrefy.users.routes import users
    # from abbrefy.links.routes import links
    # from abbrefy.links.links_api import linksApi
    # from abbrefy.users.users_api import usersApi
    # app.register_blueprint(users)
    # app.register_blueprint(links)
    # app.register_blueprint(linksApi)
    # app.register_blueprint(usersApi)

    return app
