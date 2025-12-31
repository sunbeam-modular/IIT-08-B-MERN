from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="yogeshchavan.mysql.pythonanywhere-services.com",
    user="yogeshchavan",
    password="mysqlroot",
    database="yogeshchavan$demo_db"
)

@app.route("/users")
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return jsonify(data)
