import socket
import threading
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
    if code==200 or code==201:

        def read_messages():
            while True:
                print(s.recv(1024).decode())
        thread = threading.Thread(target=read_messages)
        thread.start()

        while True:
            msg = input("Enter a message: ")
            s.sendall(str.encode(msg))
           
