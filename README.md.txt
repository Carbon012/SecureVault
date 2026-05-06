# SecureVault - SWE210 Software Security Project

## Overview
SecureVault is a secure web application developed for the SWE210 Software Security course. It functions as a mini password manager and secure notes system, built with Python and Flask. The system is designed from the ground up to demonstrate core defensive programming concepts including secure authentication, role-based access control (RBAC), and symmetric encryption.

## Core Security Features Implemented

### 1. Authentication
* **Secure Password Hashing:** Passwords are never stored in plaintext. The application utilizes `Werkzeug.security` to hash passwords using the `pbkdf2:sha256` algorithm before database insertion.
* **Session Management:** Utilizes `Flask-Login` for secure, session-based user authentication.

### 2. Role-Based Access Control (RBAC)
* **Tiered Access:** Implements two distinct user roles: `Admin` and `User`.
* **Protected Routes:** The `/admin` dashboard is strictly protected via custom middleware decorators. Unauthorized users attempting to access administrative routes are blocked with an HTTP 403 Forbidden error.

### 3. Encryption System
* **Data-at-Rest Protection:** Sensitive user data (notes/secrets) is symmetrically encrypted before being stored in the SQLite database.
* **Cryptography Implementation:** Utilizes the `cryptography` library's `Fernet` module (AES-based) for secure encryption and decryption. Data is only decrypted at the presentation layer when requested by the authorized user.

## Technology Stack
* **Backend:** Python 3, Flask
* **Database:** SQLite with SQLAlchemy ORM
* **Security:** Werkzeug (Hashing), Cryptography (Fernet/AES), Flask-Login
* **Frontend:** HTML5, Jinja2 Templating

## Local Setup & Installation
1. Clone the repository:
   ```bash
   git clone <your-github-repo-url>

2. Create and activate a virtue environment:

python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the application:

python app.py


