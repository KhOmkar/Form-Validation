# Form Validation Project

A comprehensive web form validation implementation using HTML, CSS, JavaScript, and Python Flask. This project demonstrates both client-side and server-side validation using regular expressions to validate form inputs like name, email, phone number, and password.

## Features

- Real-time form validation using JavaScript
- Server-side validation using Python Flask
- Regular expression-based validation for:
  - Name validation
  - Email validation (with specific pattern requirements)
  - Mobile number validation (10 digits starting with 6, 7, 8, or 9)
  - Password strength checker (weak, moderate, strong)
- Responsive design with user-friendly error messages
- Password strength indicator

## Project Structure

```
form_validation/
├── server.py               # Flask server for backend validation
├── README.md               # This file
└── templates/
    └── index.html          # HTML form with CSS and JavaScript
```

## Requirements

- Python 3.6+
- Flask

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/form-validation.git
cd form-validation
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install flask
```

## Running the Application

1. Start the Flask server:
```bash
python server.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

## Validation Rules

### Name Validation
- 3-50 characters long
- Only letters and spaces allowed

### Email Validation
- Must follow the pattern: `[a-z0-9][a-zA-Z0-9]{0,15}(\.[a-zA-Z]{1,15}){0,5}@[a-zA-Z]{2,15}(\.[a-zA-Z]{2,15}){1,5}`
- Examples: abc@gmail.com, abc.pqr.xyz@gmail.com

### Mobile Number Validation
- Must be exactly 10 digits
- Must start with 6, 7, 8, or 9
- Pattern: `[6-9][0-9]{9}`

### Password Strength Validation
- **Weak**: Contains lowercase letters and digits
  - Pattern: `(?=.*[a-z])(?=.*[0-9])[a-z0-9]{8,20}`
- **Moderate**: Contains lowercase, uppercase, and digits
  - Pattern: `(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,20}`
- **Strong**: Contains lowercase, uppercase, digits, and special characters
  - Pattern: `(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,20}`

## Security Features

- Data sanitization on server side
- Protection against XSS attacks
- Server-side validation to prevent tampering

## Contributors

This project was created as part of a group assignment on form validation using regular expressions.
