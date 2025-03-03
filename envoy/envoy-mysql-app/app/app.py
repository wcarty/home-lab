import os
import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify

app = Flask(__name__)

# Database configuration from environment variables
DB_HOST = os.getenv("DB_HOST", "envoy")
DB_PORT = int(os.getenv("DB_PORT", 3307))
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "mydatabase")


def get_db_connection():
    """Establish a database connection through Envoy Proxy."""
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


@app.route("/")
def home():
    return jsonify({"message": "Web App is running on port 5000!"})


@app.route("/users", methods=["GET"])
def get_users():
    """Fetch user data from the MySQL database."""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users;")
        users = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return jsonify(users)

    except Error as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Ensures it listens on all interfaces

