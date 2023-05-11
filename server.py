import socket
import threading

class Server:
    def __init__(self, ip, port):

        self.ip = ip
        self.port = port
        self.clients = {}
    
    def run(self):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self.socket.listen(5)

        while True:

            client, _ = self.socket.accept()
            client_uname = client.recv(1028).decode()

            if self.clients.get(client_uname) != None:

                client.send("Username is already taken".encode())
                client.close()
                break

            self.clients[client_uname] = client
            threading.Thread(target=self.socket_thread, args=(client_uname, client)).start()
            print(client_uname + " is Online")

    def socket_thread(self, client_uname, client):
        
        while True:

            message = client.recv(1028).decode()
            uname, message = message.split(' ', 1)
            
            if uname in self.clients.keys():
                self.clients[uname].send((client_uname + " -> " + message).encode())
            else:
                client.send("exit".encode())


server = Server("localhost", 8080)
server.run()

