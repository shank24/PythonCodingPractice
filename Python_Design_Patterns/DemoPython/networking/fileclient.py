import socket

s=socket.socket()

s.connect(('localhost',6767))

flname=input('Enter a filename')
s.send(flname.encode())
content = s.recv(1024)
print(content.decode())

s.close()
