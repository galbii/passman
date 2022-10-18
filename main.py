from passman import PassMan as pm

"""Objective No.1: create a function to take input of a master password and hash it to store it into a json file"""
    
key_path = 'public_key'

if __name__ == "__main__":
    pm = pm()
    pm.setPath(key_path)
    #key = pm.generateKey(key_path)
    #key = pm.importKey#print(pm.)
    print(pm.importKey)
    key = pm.importKey
    pm.init_fernet(key)
    pm.add_entry(b'github.com',b'hi', b'chance')
