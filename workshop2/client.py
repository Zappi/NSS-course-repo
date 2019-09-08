import socket

host = socket.gethostname()
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

msg = '---'
while(msg):
    msg = s.recv(8888).decode()
    print(msg)
s.close()
