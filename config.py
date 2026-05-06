import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Security keys should ideally be in environment variables
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-session-key-swe210'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'securevault.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Static Fernet key for development (prevents data loss on server restart)
    # Generate a new one in production using: cryptography.fernet.Fernet.generate_key()
    ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY') or b'o7yK7WqYkXZsT_3xJ5B9hE6D8A2uF1vM4jC0nN7pP-8='