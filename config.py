import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'shutdownTBSM'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:$rrsm@host:3306' + os.path.join(basedir, 'note_management_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False