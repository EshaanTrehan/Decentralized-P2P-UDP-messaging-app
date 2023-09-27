import socket
import threading 
import random
import hashlib
import getpass

#This line creates a new instance of the md5 hash algorithm from the hashlib module.

encryption=hashlib.md5()

#This line updates the hash object with the given byte string, in this case the ASCII encoded bytes of the string "password". 
# This will result in a hash that is unique to this particular input string.

encryption.update(b"password")

#This line retrieves the hexadecimal digest value of the hash object using the hexdigest() method, and then takes the first five 
# characters of the resulting string. The resulting password value is a string that consists of the first five characters of the 
# hexadecimal representation of the hash of the input string "password". This value can be used as a simple password, although it 
# is not particularly secure or strong.

password=encryption.hexdigest()[:5]

#This line creates a UDP socket object for the client and binds it to a random port number between 7000 and 9000 on the localhost

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
client.bind(("localhost", random.randint(7000, 9000)))

print("/////////////////////////////////////////////////////////////////////////")
print("            Created by Eshaan and Manasvi a P2P Chat system              ")
print("                     Welcome to the client side                          ")
print("/////////////////////////////////////////////////////////////////////////")

print("Enter Password for connection: ")
passt=getpass.getpass()

#This code checks whether the password entered by the user matches the hashed password stored in the server.

if passt==password:
    name = input("Please enter your name: ")
    target_address = None
    
    # This function keeps an eye out for new messages coming in from the P2P chat server or other clients. 
    # If the message being received is a "CONNECT" message, the target client's IP address and port number are extracted,
    # and the target address variable is set. After that, it opens a new thread to accept messages from the target client 
    # and notifies them that the current client has entered the conversation. The message is simply printed out if it is not a "CONNECT" 
    # message.
    
    def receive():
        global target_address
        while True:
            try:
                message, _ = client.recvfrom(1024)
                if message.decode().startswith("CONNECT:"):
                    target_address_str = message.decode()[len("CONNECT:"):]
                    ip = target_address_str[2:11]
                    port =  target_address_str[14:18]
                    target_address = (ip, int(port))   
                    target_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    temp = (f"{name} has joined the p2p chat!").encode()
                    target_socket.sendto(temp, target_address)
                    threading.Thread(target=receive_from_target, args=(target_socket,)).start()
                else:
                    print(message.decode())
            except:
                pass

    # This function is called in the above loop so as to recieve measssages form the target address     
    
    def receive_from_target(target_socket):
        while True:
            message, _ = target_socket.recvfrom(1024)
            print(message.decode())

    t = threading.Thread (target=receive)
    t.start()

    server_address = ("localhost", 9990)
    client.sendto(f"NAME:{name}".encode(), server_address)

    #This code runs an infinite loop that waits for the user to enter a message. If the message is "!q", it closes the client 
    # and exits the program.
    
    while True:
        message = input("")
        if message == "!q":
            client.close()
            exit()
        else:
            if target_address is not None:
                client.sendto(f"CHAT:{name}: {message}".encode(), target_address)
            else:
                client.sendto(f"CHAT:{name}: {message}".encode(), server_address)
else:
    print("Try Reconnecting again...")
            