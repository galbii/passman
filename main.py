from passman import PassMan as pm

"""Objective No.1: create a function to take input of a master password and hash it to store it into a json file"""
    
key_path = 'public_key'

if __name__ == "__main__":
    pm = pm()
    pm.add_entry('tithub', 'xgalbii', 'random password')

