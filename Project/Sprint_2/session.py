from http import server
import sqlite3
import hashlib
import socket
import threading

# Specify private IP address of accessed server here
# Current implementation is running on localhost instead
session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
session.bind(("localhost", 9999))
session.listen()

def get_login_data(conn):
    # Send username and password
    conn.send("Username: ".encode())
    username = conn.recv(1024).decode()
    conn.send("Password: ".encode())
    password = conn.recv(1024)
    
    # Get encrypted password string for comparison with value present in database
    password = hashlib.sha256(password).hexdigest

    # Pass username and password to database for verification
    conn_db = sqlite3.connect("data.db")
    cur = conn_db.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, str(password)))

    if cur.fetchall():
        conn.send("Login attempt successfull.".encode())
    else:
        conn.send("Login attempt failed.".encode())

while True:
    client, address = session.accept()
    threading.Thread(target=get_login_data, args=(client,)).start()