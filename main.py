from passman import PassMan as pm

"""Objective No.1: create a function to take input of a master password and hash it to store it into a json file"""
    
key_path = 'public_key'
def print_menu():
    choice = input("Please select an option\n\t\t1. Display website entry information\n\t\t2. Add an entry to the file.\n\t\t3. Remove and entry from the file.\n\t\t4. Clear an entry from the file\n\t\t5. Quit\n>")
    return choice

if __name__ == "__main__":
    pm = pm()
    print("Welcome to passman, a password manager that stores your data in a pandas dataframe in a file.\nYour default file will be stored in 'passwords' and you can edit them in the pasman.py file in the initializing funtion\n") 
    choice = 0
    while choice != 5:
        choice = int(print_menu())
        print(choice)
        if choice == 1:
            website = input("Please enter the website that you would like to retrieve:\n>")
            pm.get_entry(website)
        elif choice == 2:
            website = input("Website:\n")
            login = input("Login:\n")
            password = input("Password:\n")
            pm.add_entry(website, login, password)
        elif choice == 3:
            website = input("Please enter the website that you would like to delete:\n>")
            pm.del_entry(website)
        elif choice == 4:
            print('remove')
        elif choice == 5:
            pm.save_db()
