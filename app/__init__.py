from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager =LoginManager()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)

    # App configs
    app.config.from_object(config_options[config_name])

    #Init flask extensions 
    bootstrap.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    
    migrate.init_app(app, db)

    #Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Set config
    return app
