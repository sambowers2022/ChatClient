import hashlib
from getpass import getpass

def login():
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
    pwd = hashlib.sha256(pwd.encode()).hexdigest()
    print(pwd)
    return f"{opt},{user},{pwd}"

def get_credentials():
    usr = input("Username: ")
    pwd = getpass("Password: ")
    return usr, pwd

def confirm_password(pwd):
    if pwd!=getpass("Confirm password: "):
        print("Passwords do not match")
        confirm_password(pwd)
