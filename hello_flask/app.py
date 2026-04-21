# app.py

from flask import Flask
import MySQLdb
import time

app = Flask(__name__)

def connect_db():
    for i in range(10):
        try:
            db = MySQLdb.connect(
                host="mydb",
                user="root",
                passwd="my-secret-pw",
                db="mysql"
            )
            return db
        except Exception as e:
            print(f"REAL ERROR: {e}")
            time.sleep(2)
    return None


@app.route('/')
def hello_world():
    db = connect_db()
    
    if not db:
        return "❌ Failed to connect to database"

    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()

    return f"✅ Connected! MySQL version: {version[0]}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)