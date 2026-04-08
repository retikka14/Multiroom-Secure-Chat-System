# 🔐 Multi-Room Secure Chat System with File Transfer

## 📌 Overview
A secure client-server chat application supporting multiple chat rooms and encrypted file transfer using SSL/TLS. Designed to demonstrate socket programming, secure communication, and concurrent client handling.

---

## 🚀 Features
- Multi-room real-time chat
- Multiple concurrent clients
- SSL/TLS encrypted communication
- Secure file transfer
- Message broadcasting within rooms

---

## 🏗️ Architecture
**Client–Server Model**

- Server:
  - Room Management
  - Message Routing
  - File Handling
- Clients:
  - Connect via secure sockets (TLS)
  - Send/receive messages and files

---

## 🛠️ Tech Stack
- Language: Python 
- Networking: TCP Sockets
- Security: SSL/TLS

---

## ⚙️ Setup

### Clone Repo
```bash
git clone https://github.com/your-username/secure-chat-system.git
cd secure-chat-system
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Generate SSL Certificate
```bash
openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
```

### Run
```bash
# Start Server
python server/server.py

# Start Client
python client/client.py
```

---

## ▶️ Usage
1. Start server  
2. Run multiple clients  
3. Login/Register  
4. Join/Create room  
5. Chat & transfer files securely  

---
