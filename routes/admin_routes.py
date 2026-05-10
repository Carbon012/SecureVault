from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import func

from models import db
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
    total_users = User.query.count()
    failed_logins = db.session.query(func.sum(User.failed_logins)).scalar() or 0
    return render_template(
        'admin.html',
        users=users,
        total_notes=total_notes,
        total_users=total_users,
        failed_logins=failed_logins,
    )


# Add user route
from flask import request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

@admin_bp.route('/admin/add_user', methods=['POST'])
@login_required
@admin_required
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role', 'User')
    if role.lower() == 'admin':
        flash('Cannot create admin accounts from this panel.', 'danger')
        return redirect(url_for('admin.admin_dashboard'))
    if not username or not password:
        flash('Username and password required.', 'danger')
        return redirect(url_for('admin.admin_dashboard'))
    if User.query.filter_by(username=username).first():
        flash('Username already exists.', 'danger')
        return redirect(url_for('admin.admin_dashboard'))
    password_hash = generate_password_hash(password)
    user = User(username=username, password_hash=password_hash, role='User')
    db.session.add(user)
    db.session.commit()
    flash('User added successfully.', 'success')
    return redirect(url_for('admin.admin_dashboard'))

# Delete user route
@admin_bp.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.role.lower() == 'admin':
        flash('Cannot delete admin users.', 'danger')
        return redirect(url_for('admin.admin_dashboard'))
    db.session.delete(user)
    db.session.commit()
    flash('User deleted.', 'success')
    return redirect(url_for('admin.admin_dashboard'))