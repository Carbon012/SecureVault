from flask import Flask, redirect, url_for
from config import Config
from models import db
from models.user_model import User
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'error'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from routes.auth_routes import auth_bp
    from routes.user_routes import user_bp
    from routes.admin_routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    with app.app_context():
        db.create_all()
        # Auto-provision default admin account
        if not User.query.filter_by(username='admin').first():
            admin_pw = generate_password_hash('Admin123!', method='pbkdf2:sha256')
            admin_user = User(username='admin', password_hash=admin_pw, role='Admin')
            db.session.add(admin_user)
            db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)