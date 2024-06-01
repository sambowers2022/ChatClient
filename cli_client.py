import sys
from login import login
from client import SocketClient

host = len(sys.argv) > 1 and sys.argv[1] or "127.0.0.1"
port = len(sys.argv) > 2 and int(sys.argv[2]) or 65432

client = SocketClient(host, port)
code = client.auth(login())
if code == 200 or code == 201:
    client.read()
    try:
        while True:
            msg = input()
            client.send(msg)
    except KeyboardInterrupt:
        client.close()
