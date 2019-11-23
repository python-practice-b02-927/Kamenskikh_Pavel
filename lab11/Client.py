# Echo client program
import socket
import pickle

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello, world')
    data = pickle.dumps([1, 2, 228])
    s.sendall(data)
    data = s.recv(1024)
    l = pickle.loads(data)
    print('Received', l)