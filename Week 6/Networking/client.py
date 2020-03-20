import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9001))
print('Connecting to server...')

s.send(bytes('Hello World!', "utf-8"))

data = s.recv(1024)
msg = data.decode('utf-8')

if data:
    print(f'From server> {msg}')
    
s.close()