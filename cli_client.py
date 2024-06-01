from getpass import getpass
import sys
from client import SocketClient

def login(client):
    opt = input("Choose An Option ([L]ogin or [R]egister): ").lower()[0]
    if opt=="l":
        print("Login")
    elif opt=="r":
        print("Register")
    else:
        print("Invalid Option")
        login()
    
    user, pwd = get_credentials()
    if opt=="r":
        confirm_password(pwd)
    return client.auth(opt,user,pwd)

def get_credentials():
    usr = input("Username: ")
    pwd = getpass("Password: ")
    return usr, pwd

def confirm_password(pwd):
    if pwd!=getpass("Confirm password: "):
        print("Passwords do not match")
        confirm_password(pwd)

host = len(sys.argv) > 1 and sys.argv[1] or "127.0.0.1"
port = len(sys.argv) > 2 and int(sys.argv[2]) or 65432

client = SocketClient(host, port)
code = login(client)
if code == 200 or code == 201:
    client.read()
    try:
        while True:
            msg = input()
            client.send(msg)
    except KeyboardInterrupt:
        client.close()
