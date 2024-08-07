from flask import Flask, render_template
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from .routes import main_bp, profile_bp, auth_bp
app = Flask(__name__)
app.config["SECRET_KEY"] = "shutdownTBSM"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from app.routes import main_bp, profile_bp, auth_bp
app.register_blueprint(main_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(auth_bp)
if __name__ == '__main__':
    app.run(debug=True)