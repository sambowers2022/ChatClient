import socket
import hashlib
import multiprocessing

class SocketClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.process = None 
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def auth(self, opt, usr, pwd):
        if self.socket is not None:
            msg = f"{opt},{usr},{hashlib.sha256(pwd.encode()).hexdigest()}"
            self.socket.sendall(str.encode(msg))
            code = int.from_bytes(self.socket.recv(3))
            return code

    def __read_messages(self):
        while True:
            msg = self.socket.recv(1024).decode()
            print(msg)

    def read(self):
        if self.process is None:
            self.process = multiprocessing.Process(target=self.__read_messages)
            self.process.start()

    def send(self, message):
        if self.socket is not None:
            self.socket.sendall(str.encode(message))

    def close(self):
        self.socket.close()
        self.process.terminate()
