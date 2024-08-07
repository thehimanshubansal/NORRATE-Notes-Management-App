from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()

class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=4, max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save')