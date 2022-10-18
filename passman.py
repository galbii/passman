from cryptography.fernet import Fernet 
class PassMan():
    
    """Try to make it so that if you are loading this module for the first time in a folder:
        make initial init use try except
        try: searching for key file
        except(if no file found): generate a key
        read the key into a class variable self.key"""
    """Other Notes: """
    def __init__(self):
        self.password_file = "passwords"
        self.path = ""
        self.f = None
        self.key = None
        #self.generateKey(self, path)
        #might want to put this here

    def init_fernet(self, key):
        print('success')
        self.f = Fernet(key)

    def generateKey(self, path):
        self.path = path
        key = fn.generate_key()
        file = open(path, 'wb')
        file.write(key)
        file.close()

    def importKey(self):
        try:
            print(self.path)
            file = open(self.path, 'rb')
            self.key = file.read()
            self.init_fernet(self.key)
            file.close()
        except:
            print("error: public key path not defined.")

    def setPath(self, path):
        self.path = path
        print(self.path)

    """Creates an entry and appended it to the json file specified. If not password JSON file present, then the program will call init_json to create it."""
    def add_entry(self, website, login, password):
        with(open(self.password_file, 'wb')):
            epass = self.f.encrypt(password)
            elogin = self.f.encrypt(login)
            encrypted = {website: {elogin: epass}}
            file.write(enecrypted)
            print(encrypted)
            file.close()
