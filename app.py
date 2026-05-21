from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
import mysql.connector

app = Flask(__name__, static_folder='static')
CORS(app)

app.secret_key = "secretkey"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$Divya@1010",
    database="auth_system"
)

cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return send_from_directory('static', 'login.html')
# Register Page Route
@app.route('/register.html')
def register_page():
    return send_from_directory('static', 'register.html')

@app.route('/login.html')
def login_page():
    return send_from_directory('static', 'login.html')

@app.route('/dashboard.html')
def dashboard_page():
    return send_from_directory('static', 'dashboard.html')

@app.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    username = data['username']
    email = data['email']
    password = data['password']
    
    check_query = "SELECT * FROM users WHERE username=%s"
    cursor.execute(check_query, (username,))
    user = cursor.fetchone()

    if user:
        return jsonify({
            "success": False,
            "message": "Username already exists"
        })

    
    insert_query = """
    INSERT INTO users(username, email, password, role)
    VALUES(%s, %s, %s, %s)
    """

    cursor.execute(insert_query, (
        username,
        email,
        password,
        "User"
    ))

    db.commit()

    return jsonify({
        "success": True,
        "message": "Registration successful"
    })


@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    username = data['username']
    password = data['password']

    
    query = "SELECT * FROM users WHERE username=%s"

    cursor.execute(query, (username,))
    user = cursor.fetchone()

    
    if not user:

        return jsonify({
            "success": False,
            "message": "Invalid username"
        })

    
    if user['password'] != password:

        return jsonify({
            "success": False,
            "message": "Invalid password"
        })

    
    session['user'] = user['username']

    return jsonify({
        "success": True,
        "message": "Login successful"
    })



@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return jsonify({
            "success": False
        })

    username = session['user']

    query = "SELECT * FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    return jsonify({
        "success": True,
        "username": user['username'],
        "role": user['role'],
        "created_at": user['created_at']
    })



@app.route('/logout')
def logout():

    session.clear()

    return jsonify({
        "success": True
    })


if __name__ == '__main__':
    app.run(debug=True)