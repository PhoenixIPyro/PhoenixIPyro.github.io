from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from sqlalchemy import create_engine
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #name of the file that was ran
    app.config['SECRET_KEY'] = '123' #secret key
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}" #My sqlalchemy database is stored at this location
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    #Register all of them when they're added

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader #Telling flask how we load a user
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
            db.create_all(app=app)
            print('Created Database!')
