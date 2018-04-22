import os


class Config:
    '''
    Main configurations class
    '''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ramza:ramza123@localhost/blog'

    SECRET_KEY = "ramza123"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True


class ProdConfig(Config):
    '''
    Production configuration class that inherits from the main configurations class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ramza:ramza123@localhost/blog'


class DevConfig(Config):
    ''' 
    Configuration class for development stage of the app
    '''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

