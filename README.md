**Prerequisites**
1. MySQL: Make sure MySQL is installed and a database is created.
2. Python: Install Python and required libraries:

   _pip install flask mysql-connector-python_
   
     _pip install Flask-CORS_

**Step 1: Set Up the MySQL Database**

  Open MySQL Workbench or connect to MySQL in the terminal.
  Create a database and table for storing registration details.
    _CREATE DATABASE registration_db;
    USE registration_db;
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        password VARCHAR(100)
    );_

**Step 2: Set Up the Flask API**

  This Flask API will handle POST requests from the frontend and insert user data into the database.
    Create a file called app.py
  Explanation:
    The /register route expects a JSON payload with name, email, and password.
    After receiving the data, it inserts it into the users table in MySQL.

**Step 3: Set Up the HTML Form**

  Create an HTML form (index.html) that will submit data to the API.
Explanation:
  The form collects user information (name, email, password).
  The registerUser JavaScript function sends this data as JSON to the /register API.

**Step 4: Run the API and Test the Application**

  Start the Flask API server:
    _python app.py_
  This should start the server at http://127.0.0.1:5000.
  Open index.html in a browser (e.g., by opening the file directly or using a server like http-server for local testing).

Fill out the form and click “Register.” If successful, you should see a message confirming the registration.
