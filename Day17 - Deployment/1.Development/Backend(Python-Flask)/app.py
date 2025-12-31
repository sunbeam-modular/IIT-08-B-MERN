from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="demo_db"
)

@app.route("/users")
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run()
