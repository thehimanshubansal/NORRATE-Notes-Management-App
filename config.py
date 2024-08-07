import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'shutdownTBSM'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'note_management_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False