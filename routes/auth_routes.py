from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from models.user_model import User
from utils.security import check_password_strength

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return redirect(url_for('auth.register'))

        if not check_password_strength(password):
            flash('Password must be at least 8 characters, containing uppercase, lowercase, and numbers.', 'error')
            return redirect(url_for('auth.register'))

        # Secure Hashing Implementation
        hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password_hash=hashed_pw, role='User')

        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user:
            # Basic brute-force protection logic
            if user.failed_logins >= 5:
                flash('Account locked due to multiple failed login attempts.', 'error')
                return redirect(url_for('auth.login'))

            if check_password_hash(user.password_hash, password):
                user.failed_logins = 0 
                db.session.commit()
                login_user(user)
                if user.role == 'Admin':
                    return redirect(url_for('admin.admin_dashboard'))
                return redirect(url_for('user.dashboard'))
            else:
                user.failed_logins += 1
                db.session.commit()

        flash('Invalid credentials.', 'error')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))