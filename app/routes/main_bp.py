from flask import render_template, request, redirect, url_for, flash
from . import main_bp
from ..forms import LoginForm

@main_bp.route('/')
def index():
    return render_template('index.html', title='Home')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process login logic here (e.g., authenticate user, redirect)
        flash('Login successful', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Login', form=form)