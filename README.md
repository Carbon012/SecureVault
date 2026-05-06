🔐 SecureVault
SecureVault is a modular Flask-based web application designed for secure note-taking. It implements industry-standard security practices, including hashed password storage, role-based access control (RBAC), and brute-force protection.

🚀 Features
• User Authentication: Secure registration and login using Flask-Login.
• Password Security: Industry-standard hashing via Werkzeug.
• Brute-Force Protection: Automatic account lockout after 5 failed login attempts.
• Role-Based Access Control (RBAC): Distinct permissions for User and Admin accounts.
• Admin Dashboard: Centralized view for managing users and monitoring system stats.
• Database: Persistent storage using SQLite.

🛠️ Tech Stack
• Backend: Python (Flask)
• Database: SQLite / SQLAlchemy (ORM)
• Security: Flask-Login, Werkzeug (Hashing), Custom Decorators
• Frontend: Jinja2 Templates, CSS3

📦 Project Structure
SecureVault/
├── models/             # Database schemas (User, Note)
├── routes/             # Blueprint-based routing (Auth, Admin, User)
├── static/             # CSS and Assets
├── templates/          # HTML files (Login, Register, Dashboard)
├── utils/              # Security decorators and helper functions
├── app.py              # Main application entry point
├── config.py           # Configuration settings
└── securevault.db      # SQLite Database

⚙️ Installation & Setup
1.Clone the repository:
git clone https://github.com/Carbon012/SecureVault.git
cd SecureVault
2.Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install dependencies:
pip install -r requirements.txt
4. Run the application:
python app.py
Access the app at http://127.0.0.1:5000

🛡️ Security Implementation Details
• Account Lockout: If a user provides an incorrect password 5 times, the failed_logins counter triggers a lockout. Only an administrator can reset this counter via the database.
• Route Protection: The @admin_required decorator ensures that sensitive endpoints (like the Admin Dashboard) are inaccessible to standard users, even if they are logged in.
Developed by Hammad Cybersecurity & Software Engineering Student
