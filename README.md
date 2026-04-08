# Multi-Client Chat Application

## Overview
This project is a TCP-based client–server chat application that supports multiple clients simultaneously. It includes chat rooms, private messaging, file transfer, and secure communication using SSL/TLS.

## Features
- Multi-client support using threading  
- Multiple chat rooms  
- Private messaging between users  
- File transfer capability  
- Secure communication with SSL/TLS  

## Technologies Used
- Python (Sockets, Threading, SSL)
- TCP/IP Protocol

## Project Structure
```
/project-folder
│── server.py
│── client.py
│── ssl_cert.pem
│── ssl_key.pem
│── README.md
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project-folder
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the Server
```bash
python server.py
```

### Start the Client
```bash
python client.py
```

## How It Works
- The server listens for incoming client connections.
- Each client is handled in a separate thread.
- Users can join chat rooms or send private messages.
- Files can be transferred between clients.
- SSL/TLS ensures encrypted communication.

## Security
- Uses SSL/TLS for encrypted data transmission.
- Requires certificate and key files (`ssl_cert.pem`, `ssl_key.pem`).


## License
This project is for educational purposes.
