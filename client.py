# Import required libraries
import socket
import threading
import ssl

# Server details
HOST = "127.0.0.1"
PORT = 5555

# Ask user for username
name = input("Enter your name: ")

# Create SSL context
context = ssl.create_default_context()

# Disable certificate verification (for testing)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap socket with SSL encryption
client = context.wrap_socket(sock, server_hostname=HOST)

# Connect to server
client.connect((HOST, PORT))

# Send username to server
client.send(name.encode())

# Function to receive messages from server
def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            break

# Run receiving function in separate thread
threading.Thread(target=receive).start()

# Main loop for sending commands
while True:

    cmd = input()

    # FILE SEND COMMAND
    if cmd.startswith("FILE:"):

        parts = cmd.split(":")
        filename = parts[2]

        # Send command first
        client.send(cmd.encode())

        # Read file data
        with open(filename, "rb") as f:
            data = f.read()

        # Send file content
        client.send(data)

    else:
        # Send normal command
        client.send(cmd.encode())