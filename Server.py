import socket

serversocket = socket.socket()
host = socket.gethostname()
port = 8080
serversocket.bind((host, port))

print("waiting for a connection")
serversocket.listen(5)

conn, addr = serversocket.accept()
print("Got connection from", addr)

file = open('Code.jpg', 'rb')
data = file.read()

while data:
    conn.send(data)
    data = file.read()

file.close()
print("Succesfully Transfered")








