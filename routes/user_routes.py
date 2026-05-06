from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.note_model import Note
from utils.encryption import encrypt_data, decrypt_data

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        secret_text = request.form.get('secret_text')
        if secret_text:
            # Encrypt prior to database insertion
            encrypted_text = encrypt_data(secret_text)
            new_note = Note(user_id=current_user.id, encrypted_content=encrypted_text)
            db.session.add(new_note)
            db.session.commit()
            flash('Note securely encrypted and stored.', 'success')

    user_notes = Note.query.filter_by(user_id=current_user.id).all()
    decrypted_notes = []
    
    # Decrypt only at presentation layer
    for note in user_notes:
        try:
            decrypted_content = decrypt_data(note.encrypted_content)
            decrypted_notes.append({'id': note.id, 'content': decrypted_content})
        except Exception:
            decrypted_notes.append({'id': note.id, 'content': '[Decryption Error]'})

    return render_template('dashboard.html', notes=decrypted_notes)

@user_bp.route('/delete_note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    # Ensure users can only delete their own notes
    if note.user_id != current_user.id:
        flash('Unauthorized action.', 'error')
        return redirect(url_for('user.dashboard'))

    db.session.delete(note)
    db.session.commit()
    flash('Note deleted.', 'success')
    return redirect(url_for('user.dashboard'))