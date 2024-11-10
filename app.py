from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',       # Replace with your MySQL username
    'password': 'sagar',  # Replace with your MySQL password
    'database': 'registrationdb'
}

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        # Get data from request
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Insert data into database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
