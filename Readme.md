# Contact Management Portal

A secure Contact Management Portal built using Flask and MySQL with authentication, role-based access control, layered architecture, CSRF protection, validation, and audit logging.



# Features

## Authentication
- User Registration
- User Login
- Password Hashing using Werkzeug
- Session Management
- Logout Functionality

## Security
- CSRF Protection using Flask-WTF
- Password Strength Validation
- Email Validation
- Empty Field Validation
- Audit Logging
- Environment Variable Configuration

## Contact Management
- Add Contacts
- View Contacts
- Delete Contacts
- User-specific Contact Access

## Admin Features
- Admin Dashboard
- View All Users
- View All Contacts
- Role-Based Access Control (RBAC)



# Project Structure

```bash
Project/
│
├── repositories/
│   ├── auth_repository.py
│   └── contact_repository.py
│
├── routes/
│   ├── auth_routes.py
│   ├── dashboard_routes.py
│   └── admin_routes.py
│
├── services/
│   ├── auth_service.py
│   └── contact_service.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── admin.html
│
├── utils/
│   ├── logger.py
│   └── validators.py
│
├── logs/
│   └── audit.log
│
├── .env
├── .gitignore
├── app.py
├── db.py
└── README.md
```



# Technologies Used

- Python
- Flask
- MySQL
- Flask-WTF
- HTML
- CSS



# Setup Instructions

## 1. Clone Repository


git clone <repository-url>





## 3. Install Dependencies


- Present in the Requirements.txt file can run the while cloning the repo → pip install -r requirements.txt




## 4. Configure Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key
```



## 5. Run Application


python app.py



# Database Tables

## Users Table
"""
- CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20) DEFAULT 'user'
    
); 

"""


## Contacts Table
"""
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    phone VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""
# Security Implementations

- Passwords stored as hashed values
- CSRF protection for all forms
- Session-based authentication
- User authorization checks
- Secure environment variables
- Audit logging for login/logout activities



# Future Improvements

- Google OAuth Login
- Edit Contact Feature
- Pagination







# Author

Developed as a backend-focused Flask learning project with layered architecture and security best practices.
