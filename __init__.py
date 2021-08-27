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
mail = Mail()

# setting up CORS
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    mail.init_app(app)

    from routes import main, page_not_found
    app.register_blueprint(main)
    app.register_error_handler(404, page_not_found)

    return app
