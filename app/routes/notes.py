from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import NoteForm
from app.models import Note
from flask import abort, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes', methods=['GET'])
@login_required
def index():
    notes = current_user.notes.all()
    return render_template('notes.html', title='Notes', notes=notes)

@notes_bp.route('/notes/new', methods=['GET', 'POST'])
@login_required
def new_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(title=form.title.data, content=form.content.data, user=current_user)
        db.session.add(note)
        db.session.commit()
        flash('Note created successfully!')
        return redirect(url_for('notes.index'))
    return render_template('new_note.html', title='New Note', form=form)

@notes_bp.route('/notes/<int:note_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user != current_user:
        abort(403)
    form = NoteForm()
    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        db.session.commit()
        flash('Note updated successfully!')
        return redirect(url_for('notes.index'))
    elif request.method == 'GET':
        form.title.data = note.title
        form.content.data = note.content
    return render_template('edit_note.html', title='Edit Note', form=form)

@notes_bp.route('/notes/<int:note_id>/delete', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user != current_user:
        abort(403)
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted successfully!')
    return redirect(url_for('notes.index'))