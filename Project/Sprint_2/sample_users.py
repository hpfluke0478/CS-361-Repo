import sqlite3
import hashlib

connection = sqlite3.connect("data.db")
session = connection.cursor()

session.execute("""
CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KET,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
)
""")

user1, pass1 = "henry21", hashlib.sha256("mypassword".encode()).hexdigest()

print(pass1)