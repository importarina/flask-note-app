from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .. import db
import json
# views is a Blueprint of our app, meaning it has a roots/urls defined inside it
# so we don't have all of our views in one file, and we can split them up into multiple
# files in an organized way.
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required  # cannot get to the homepage unless logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash("Note is too short.", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category='success')
    # then go back to the homepage and render that note
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})


@views.route('/update', methods=['GET', 'POST'])
def update_note():
    if request.method == 'POST':
        updating_note = Note.query.get(request.form.get('updatingNoteId'))
        if updating_note:
            if updating_note.user_id == current_user.id:
                db.session.delete(updating_note)
                db.session.commit()
                note = request.form.get('updatingNote')
                if len(note) < 1:
                    flash("Note is too short.", category='error')
                else:
                    new_note = Note(data=note, user_id=current_user.id)
                    db.session.add(new_note)
                    db.session.commit()
                    flash("Note updated!", category='success')
    return render_template("home.html", user=current_user)
