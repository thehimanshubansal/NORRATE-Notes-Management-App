from flask import Flask, render_template, jsonify
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from .routes import main_bp, profile_bp, auth_bp
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "shutdownTBSM"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:$rrsm@localhost:3306/norrate'

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from app.routes import main_bp, profile_bp, auth_bp
app.register_blueprint(main_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(auth_bp)

def index():
    return jsonify(message="Welcome to Norrate Note Management App!")
if __name__ == '__main__':
    app.run(debug=True)