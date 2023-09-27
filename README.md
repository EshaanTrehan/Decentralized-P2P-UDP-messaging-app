
# Decentralized P2P UDP Messaging App 📬

Welcome to **Decentralized P2P UDP Messaging App**, a Python-based application that offers a decentralized approach to peer-to-peer messaging over the UDP protocol. The application ensures direct communication between clients without the need for a central messaging server after initial connection setup.

## 🚀 Features

- **Decentralized Communication**: After the initial connection setup via the server, clients communicate directly with each other.
- **UDP Protocol**: Utilizes the User Datagram Protocol (UDP) for message transmission.
- **Password Protection**: Uses MD5 hashing for a basic level of password encryption.
- **Threaded Design**: Employs multiple threads for seamless message sending, receiving, and broadcasting.

## 📁 File Structure

- 📄 `finalclient.py`: Client-side implementation. Handles client operations like sending and receiving messages.
- 📄 `finalserver.py`: Server-side logic. Manages connected clients, broadcasts messages, and facilitates P2P connections.

## 🔧 Setup & Execution

1. Start the server:
   ```bash
   python finalserver.py
   ```
2. On the client side, run:
   ```bash
   python finalclient.py
   ```
3. Follow the on-screen prompts to enter your password and name.
4. Begin messaging! 

## 🧠 Technical Details

- **Encryption**: The application uses MD5 hashing for password encryption, offering a basic level of security.
- **Data Transmission**: The UDP protocol is adopted for its connectionless nature, ensuring lightweight and fast communication.
- **Decentralization**: After clients connect through the main server, direct P2P connections are established for decentralized messaging.

## 🧪 Testing

1. Start the server script.
2. Launch multiple client scripts from different terminals or machines.
3. Connect each client by providing the necessary details.
4. Send messages between clients to test the P2P functionality and observe the direct communication.
5. 
