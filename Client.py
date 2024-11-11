import socket
import time

class Client:
    def run(self):
        while True:
            print("Welcome to TanCheatCode")
            try:
                socketclient = socket.socket()
                host = "DarkGlitch"
                port = 8080
                socketclient.connect((host, port))
                print("Connected to Server")

                file = open('Tan.jpg', 'wb')

                while True:
                    data = socketclient.recv(1024)
                    while data:
                        file.write(data)
                        data = socketclient.recv(1024)
                file.close()
                print("File successfully transfered")
                break

            except Exception as e:
                print("Can't connect to server")
                time.sleep(10)


Client.run(0)