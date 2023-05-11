import socket
import threading

def reciving_messages():
    global client
    while True:
        message = client.recv(1024).decode()
        print(message)


port = 8080
uname = input("Your Username :")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", port))
client.send(uname.encode())

threading.Thread(target=reciving_messages).start()

while True:

    print("Type Friend's Username to start the session and 'exit' to end the session")
    friend_uname = input()

    while True:

        message = input()

        if message == "exit":
            break

        client.send((friend_uname + " " + message).encode())

