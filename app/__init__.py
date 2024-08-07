from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

# Register the blueprints
from .routes import main_bp, auth_bp
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)


db = SQLAlchemy(app)

from app import routes, models