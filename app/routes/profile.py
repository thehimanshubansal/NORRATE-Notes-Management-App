from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import UserProfileForm
from app.models import User
from flask_sqlalchemy import SQLAlchemy
from app.forms import PasswordForm
from app import db

# db = SQLAlchemy(app)1
profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def index():
    form = UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('profile.index'))
    return render_template('profile.html', title='Profile', form=form)

@profile_bp.route('/profile/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = PasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.old_password.data):
            flash('Old password is incorrect')
            return redirect(url_for('profile.change_password'))
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('Password changed successfully!')
        return redirect(url_for('profile.index'))
    return render_template('change_password.html', title='Change Password', form=form)