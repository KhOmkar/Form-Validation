# server.py - Server-side validation using Flask
from flask import Flask, request, render_template, jsonify
import re

app = Flask(__name__)

# Regex patterns based on provided rules
NAME_REGEX = re.compile(r'^[a-zA-Z\s]{3,50}$')
EMAIL_REGEX = re.compile(r'^[a-z0-9][a-zA-Z0-9]{0,15}(\.[a-zA-Z]{1,15}){0,5}@[a-zA-Z]{2,15}(\.[a-zA-Z]{2,15}){1,5}$')
PHONE_REGEX = re.compile(r'^[6-9][0-9]{9}$')
WEAK_PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[0-9])[a-z0-9]{8,20}$')
MODERATE_PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,20}$')
STRONG_PASSWORD_REGEX = re.compile(r'^(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,20}$')

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML form

@app.route('/register', methods=['POST'])
def register():
    # Get form data
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirmPassword', '')
    
    # Initialize errors dictionary
    errors = {}
    
    # Validate name
    if not NAME_REGEX.match(name):
        errors['name'] = "Name must be 3-50 characters long and contain only letters and spaces."
    
    # Validate email
    if not EMAIL_REGEX.match(email):
        errors['email'] = "Please enter a valid email address."
    
    # Validate phone
    if not PHONE_REGEX.match(phone):
        errors['phone'] = "Please enter a valid 10-digit mobile number starting with 6, 7, 8, or 9."
    
    # Validate password
    if len(password) < 8 or len(password) > 20:
        errors['password'] = "Password must be 8-20 characters."
    elif not (WEAK_PASSWORD_REGEX.match(password) or MODERATE_PASSWORD_REGEX.match(password) or STRONG_PASSWORD_REGEX.match(password)):
        errors['password'] = "Password must contain at least lowercase letters and digits."
    
    # Check password strength
    password_strength = ""
    if STRONG_PASSWORD_REGEX.match(password):
        password_strength = "strong"
    elif MODERATE_PASSWORD_REGEX.match(password):
        password_strength = "moderate"
    elif WEAK_PASSWORD_REGEX.match(password):
        password_strength = "weak"
    
    # Validate confirm password
    if password != confirm_password:
        errors['confirmPassword'] = "Passwords do not match."
    
    # If there are validation errors, return them
    if errors:
        return jsonify({
            'success': False,
            'errors': errors,
            'password_strength': password_strength
        }), 400
    
    # Data sanitization (to prevent XSS attacks)
    name = name.strip()
    email = email.lower().strip()
    
    # Process form data (in a real application, you would save to database here)
    # For this example, we're just returning success
    return jsonify({
        'success': True,
        'message': 'Registration successful!',
        'data': {
            'name': name,
            'email': email,
            'phone': phone,
            'password_strength': password_strength
        }
    })

if __name__ == '__main__':
    app.run(debug=True)