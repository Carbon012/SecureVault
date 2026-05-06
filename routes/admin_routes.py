from flask import Blueprint, render_template
from flask_login import login_required
from models.user_model import User
from models.note_model import Note
from utils.security import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()
    total_notes = Note.query.count()
    return render_template('admin.html', users=users, total_notes=total_notes)