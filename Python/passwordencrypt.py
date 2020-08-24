import json

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

#read contents from json file
def _read(account,ID):
    try:
        fp = open("passwords.json","r")
        obj = json.load(fp)
    except:
        __init__()
        fp = open("passwords.json","r")
        obj = json.load(fp)
    finally:
        fp.close()
        return obj.get(account).get(ID) 
            
#write contents to json file
def _write(account,ID,Pass):
    try:
        fp = open("passwords.json","r")
        obj = json.load(fp)
    except:
        __init__()
        fp = open("passwords.json","r")
        obj = json.load(fp)

    finally:
        fp.close()

    try:
        fp = open("passwords.json","w")
        
        if account not in obj.keys():
            obj[account] = {ID:Pass}
            
        elif account in obj.keys():
            
            if ID not in obj[account]:
                obj[account][ID] = Pass
                print("Password added.")
                print(f"{account}\n{ID}:{password}")
            
            elif ID in obj[account]:
                print("Password found.")
                print("Changing password...")
                print("Old passsword is: ",obj[account][ID])
                obj[account][ID] = Pass
                print("Password changed.")
        
        fp.write(json.dumps(obj,indent = 4))

    finally:
        fp.close()

#create an empty json file
def __init__():

    try:
        fp = open("passwords.json","w")
        data = {}
        fp.write(json.dumps(data,indent=4))
    finally:
        fp.close()

while True:
    #Mode
    mode = input("Enter mode['encrypt','e','decrypt','d','change','c']: ").lower()
    
    if mode[0] in ['e','c']:
        account = input("Enter the account name: ")
        ID = input("Enter account ID: ")
        password = input("Enter the {}password: ".format('' if mode[0] == 'e' else 'new ')).encode()

    elif mode[0] == 'd':
        account = input("Enter the required account name: ")
        ID = input("Enter ID: ")

    else:
        print("Mode unidentified.")
        continue

    key = input("Enter the key: ").encode()
    salt = b'SALT' #can be anything else as 'SALT' as mentioned here But should be same always while encrypting and decrypting.
    kdf = kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )
    _key = base64.urlsafe_b64encode(kdf.derive(key))

    f = Fernet(_key)

    if mode[0] in ['e','c']:
        Pass = f.encrypt(password) #Encrypt password with encrypt() method
        print(f"Encrypted.\n{account}\n{ID}: {Pass}") #print encrypted passwrod with account name and ID.
        _write(account,ID,Pass.decode()) #save to json file.

    elif mode[0] == 'd':
        try:
            password = _read(account,ID) #read password from json file.
            if password is None:
                print("Password not found.")
                continue
                
            Pass = f.decrypt(password.encode()) #Decrypt password with decrypt() method.
            print(f"Decrypted.\n{account}\n{ID}: {Pass.decode()}") #print decrypted password with account name and ID.
        
        except AttributeError:
            print("Can't find account.") #if account name is not in the file
            
        except:
            print("Sorry! key didn't match.\nEnter correct key.") #if key didn't match

