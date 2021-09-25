import pymysql
import pymysql.cursors
from flask import jsonify
from app import app
from db import mysql

@app.route('/')
def users():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM user")

    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200

    return resp

@app.route('/kt', methods=['GET'])
def kent():
    return '<h1>HEJ KENT!</h1>'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')