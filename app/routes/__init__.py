from flask import Flask
from flask import Blueprint


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

# Create a Blueprint for the main routes
main_bp = Blueprint('main', __name__, template_folder='templates')

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__, template_folder='templates')


# from . import main_bp
# from . import auth_bp