import os


class Config:
    '''
    Main configurations class
    '''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Ivonne1236987@localhost:1234/blog'

    SECRET_KEY = "wasdertyuiop"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
    '''
    Production configuration class that inherits from the main configurations class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    ''' 
    Configuration class for development stage of the app
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Ivonne1236987@localhost:1234/blog'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

