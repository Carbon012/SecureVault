
# 🔐 SecureVault

SecureVault is a secure, modular web application for managing encrypted notes and user accounts. Built with Flask, it demonstrates best practices in authentication, RBAC, brute-force protection, and data encryption—making it ideal for learning and real-world secure note management.

---

## 🚀 Features

- **User Authentication:** Secure registration and login with hashed passwords (Werkzeug, Flask-Login).
- **Brute-Force Protection:** Accounts are locked after 5 failed login attempts.
- **Role-Based Access Control:** Separate roles for Admin and User, with strict route protection.
- **Admin Dashboard:** View system stats, manage users, and monitor failed login attempts.
- **User Management:** Admins can add or delete users (except other admins).
- **Encrypted Notes:** All notes are encrypted at rest using AES (Fernet).
- **Flash Messaging:** Modern, animated pop-up notifications for all actions.
- **Responsive UI:** Clean, accessible interface with clear feedback.

---

## 🏗️ Project Structure

```
SecureVault/
├── app.py                # Application factory and entry point
├── config.py             # Configuration (secret keys, etc.)
├── requirements.txt      # Python dependencies
├── models/
│   ├── __init__.py       # SQLAlchemy instance
│   ├── user_model.py     # User schema and logic
│   └── note_model.py     # Note schema and logic
├── routes/
│   ├── __init__.py
│   ├── admin_routes.py   # Admin dashboard and user management
│   ├── auth_routes.py    # Registration, login, logout
│   └── user_routes.py    # User dashboard and note management
├── utils/
│   ├── __init__.py
│   ├── encryption.py     # Fernet-based encryption helpers
│   └── security.py       # RBAC decorators, password checks
├── templates/
│   ├── base.html         # Main layout
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── dashboard.html    # User dashboard
│   └── admin.html        # Admin dashboard
├── static/
│   └── style.css         # Custom CSS
└── securevault.db        # SQLite database (auto-created)
```

---

## 🛡️ Security Architecture

- **Password Hashing:** All passwords are hashed with PBKDF2 (sha256) before storage.
- **Session Management:** Flask-Login ensures secure session handling.
- **RBAC:** Custom decorators enforce admin-only access to sensitive routes.
- **Brute-Force Lockout:** After 5 failed logins, accounts are locked until admin resets.
- **Encryption:** Notes are encrypted using Fernet (AES) before being saved.
- **Cascading Deletes:** Deleting a user also deletes their notes, preventing orphaned data.

---

## ⚙️ Setup & Installation

1. **Clone the repository:**
	```bash
	git clone https://github.com/YourUsername/SecureVault.git
	cd SecureVault
	```

2. **Create and activate a virtual environment:**
	```bash
	python -m venv venv
	# On Windows:
	venv\Scripts\activate
	# On Mac/Linux:
	source venv/bin/activate
	```

3. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```

4. **Run the application:**
	```bash
	python app.py
	```
	The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

5. **Default Admin Account:**
	- On first run, an admin account is auto-created:
	  - Username: `admin`
	  - Password: `Admin123!`
	- Change this password after first login for security.

---

## 🖥️ How It Works

- **Login/Registration:** Users register and log in securely. Passwords are never stored in plaintext.
- **User Dashboard:** Users can create, view, and manage their encrypted notes.
- **Admin Dashboard:** Admins see system stats, failed login attempts, and manage users.
- **User Management:** Admins can add or delete users (but not other admins).
- **Security Feedback:** All actions provide clear, animated feedback via pop-up messages.
- **Brute-Force Monitoring:** The admin dashboard shows total failed login attempts for all users.

---

## 🧑‍💻 Development & Customization

- All configuration is in `config.py`.
- Add new features by extending the `routes/`, `models/`, or `utils/` modules.
- UI is built with Jinja2 templates and CSS for easy customization.

---

## 📄 License

This project is for educational and demonstration purposes. For production use, review and enhance all security settings.

---

## 👤 Author

Developed by Hammad — Cybersecurity & Software Engineering Student
