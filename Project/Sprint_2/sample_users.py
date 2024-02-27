import sqlite3
import hashlib

connection = sqlite3.connect("data.db")
session = connection.cursor()

session.execute("""
CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
)
""")

user1, pass1 = "henry21", hashlib.sha256("mypassword".encode()).hexdigest()
user2, pass2 = "candice34", hashlib.sha256("password123".encode()).hexdigest()
user3, pass3 = "joe54", hashlib.sha256("evilbrandon".encode()).hexdigest()
user4, pass4 = "agent47", hashlib.sha256("isthisasecurepassword".encode()).hexdigest()

session.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user1, pass1))
session.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user2, pass2))
session.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user3, pass3))
session.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user4, pass4))

connection.commit()