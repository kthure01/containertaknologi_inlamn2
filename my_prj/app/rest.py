import pymysql
import pymysql.cursors
from flask import render_template, request, jsonify
from app import app
from db import mysql


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Not valid"

    conn = mysql.connect()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO user(name, age) VALUES(%s, %s)", (name, age))
        conn.commit()
        cursor.close()
        return f"Done!!"


@app.route('/show_db', methods=['POST', 'GET'])
def show_db():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM user")

    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200

    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0')
