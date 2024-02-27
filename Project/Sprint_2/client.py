from email import message
import re
import socket

# Specify public IP address of accessed server here
# Current implementation is running on localhost instead
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

# Get username from user
message = client.recv(1024).decode()
client.send(input(message).encode())

# Get password from user
message = client.recv(1024).decode()
client.send(input(message).encode())

# Print server response
print(client.recv(1024).decode())