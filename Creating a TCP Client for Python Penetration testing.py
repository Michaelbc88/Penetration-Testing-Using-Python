import socket

clientsocket = socket.socket(socket.AF_INET,socket.sock_STREAM)

host = socket.gethostname()

port = 444 

clientsocket.connect(('192.168.1.104', part))

message = clientsocket.connect.recv(1024)

clientsocket.close()

print(message.decode('ascii'))