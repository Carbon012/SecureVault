from functools import wraps
from flask_login import current_user
from flask import abort
import re

def admin_required(f):
    """Middleware decorator to strictly enforce RBAC."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'Admin':
            abort(403) # Forbidden
        return f(*args, **kwargs)
    return wrapper

def check_password_strength(password: str) -> bool:
    """Advanced: Validates password strength complexity."""
    if len(password) < 8: return False
    if not re.search(r"[A-Z]", password): return False
    if not re.search(r"[a-z]", password): return False
    if not re.search(r"[0-9]", password): return False
    return True