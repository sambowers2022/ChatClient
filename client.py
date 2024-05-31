import socket
from login import login
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
token = None
# Create Connection
auth = login()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str.encode(auth))
    code = int.from_bytes(s.recv(3))
    print(f"Received {code}")
    if code==400:
        token = s.recv(1024)
