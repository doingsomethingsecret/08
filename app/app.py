import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "appdb")
DB_USER = os.environ.get("DB_USER", "appuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "apppassword")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


@app.route("/")
def home():
    return jsonify(message="Hello from Flask! Dummy app for Assignment 08.")


@app.route("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify(status="connected", postgres_version=version[0])
    except Exception as e:
        return jsonify(status="error", detail=str(e)), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)