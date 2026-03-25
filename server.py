# Import required libraries
import socket          # For TCP socket communication
import threading       # For handling multiple clients simultaneously
import ssl             # For secure TLS communication
import os              # For file operations
import re              # For validating room names

# Server configuration
HOST = "127.0.0.1"     # Localhost address
PORT = 5555            # Port number server listens on

# Dictionaries to store connected clients and chat rooms
clients = {}           # {username : socket}
rooms = {}             # {room_name : [client sockets]}

# Create folder for storing received files
if not os.path.exists("received_files"):
    os.makedirs("received_files")

# Function to validate room names (only letters, numbers, underscore allowed)
def valid_room(room):
    return re.match("^[A-Za-z0-9_]+$", room)

# Function to broadcast messages to all clients in a room
def broadcast(room, message, sender=None):
    if room in rooms:
        for client in rooms[room]:
            if client != sender:      # Do not send message back to sender
                client.send(message.encode())

# Function that handles each connected client
def handle_client(conn, addr):

    # Receive username from client
    name = conn.recv(1024).decode()
    clients[name] = conn

    print(f"{name} connected from {addr}")

    while True:
        try:
            # Receive command from client
            data = conn.recv(1024).decode()

            if not data:
                break

            # JOIN ROOM COMMAND
            if data.startswith("JOIN:"):

                room = data.split(":")[1]

                # Validate room name
                if not valid_room(room):
                    conn.send("SERVER: Invalid room name".encode())
                    continue

                # Create room if it doesn't exist
                if room not in rooms:
                    rooms[room] = []

                # Add client to room
                rooms[room].append(conn)

                conn.send(f"SERVER: Joined {room}".encode())

                # Notify other users
                broadcast(room, f"SERVER: {name} joined {room}", conn)


            # ROOM MESSAGE COMMAND
            elif data.startswith("MSG:"):

                parts = data.split(":",2)
                room = parts[1]
                msg = parts[2]

                # Send message to everyone in the room
                broadcast(room, f"{name}: {msg}", conn)


            # PRIVATE MESSAGE COMMAND
            elif data.startswith("PM:"):

                parts = data.split(":",2)
                target = parts[1]
                msg = parts[2]

                # Send message directly to target user
                if target in clients:
                    clients[target].send(f"[PM from {name}] {msg}".encode())
                else:
                    conn.send("SERVER: User not found".encode())


            # FILE TRANSFER COMMAND
            elif data.startswith("FILE:"):

                parts = data.split(":")
                room = parts[1]
                filename = parts[2]

                # Receive file data
                filedata = conn.recv(4096)

                path = os.path.join("received_files", filename)

                # Save file on server
                with open(path, "wb") as f:
                    f.write(filedata)

                # Notify room users
                broadcast(room, f"[FILE] {name} sent file {filename}")


            # CLIENT EXIT
            elif data == "QUIT":
                break

            else:
                conn.send("SERVER: Invalid command".encode())

        except:
            break

    conn.close()
    print(f"{name} disconnected")


# Function to start the chat server
def start_server():

    # Create SSL context for secure communication
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    # Load certificate and private key
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    # Create TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind server to IP and port
    server.bind((HOST, PORT))

    # Listen for incoming client connections
    server.listen()

    print("Secure Chat Server started...")

    while True:

        # Accept new client connection
        client_socket, addr = server.accept()

        # Wrap socket with SSL/TLS encryption
        secure_conn = context.wrap_socket(client_socket, server_side=True)

        # Create new thread to handle client
        thread = threading.Thread(target=handle_client, args=(secure_conn, addr))
        thread.start()

# Start server
start_server()