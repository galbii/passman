import pandas as pd
from typing import Optional
class PassMan():
    
    """Initial Init to create a passman object. Creates the password file and stores it in self.password_file. Self.key will be"""
    def __init__(self):
        self.password_file = "passwords"
        try:
            self.passtable = pd.read_csv(self.password_file, index_col = 0)
        except:
            self.passtable = pd.DataFrame(data = None, columns = ['Login', 'Password'])
        self.path = "public_key"
        self.key = None

    def save_db(self):
        self.passtable.to_csv(self.password_file)
        print('[success] thank you for using passman')
    
    #def inc_dig(dig):
    """edit this function to manually check if an entry is correct see test.py to see the test results i.e. df.loc['ya', 'hii'] == entry['hii'] food for thought, assign df.loc[certain_entry] to a variable and then do comparisons with single row values"""
    def get_entry(self, website):
        try:
            print(self.passtable.loc[website])
        except:
            print("[error] entry not found")

    def check_entry(self, web, entry, mode : Optional[str]="unmatch"):
        if web in self.passtable.index:
            print('bitch')
            """This if statement check to see if the entry login and password matches"""
            if self.passtable.loc[web]["Login"] == entry[0] and self.passtable.loc[web]["Password"] == entry[1] and mode == "match":
                return True
            elif mode == "unmatch":
                return True
            elif mode == "match":
                return False 
            else:
                return False
        else:
            return False
        
        """gonna make it so that only one single instance of the website will
        be accomodated for
        edit: lol good luck figuring out what this function does xdxdxdxd"""
    def add_entry(self, website, login, password):
        entry = [login, password]
        #print(df.loc[website][["Login","Password"]] )
        #df.loc[website] = [login, password]
        if self.check_entry(website, entry):
            if self.check_entry(website, entry, mode = "match"):
                print('Entry is already added')
            elif not self.check_entry(website+"1", entry, mode = "match"):
                """ovverride needed here define override function tomorrow"""
                self.passtable.loc[website + str(int(website[-1])+1)] = entry
                print("you're gay")
            else:
                self.passtable.loc[website+'1'] = entry
        else:
            self.passtable.loc[website] = entry
#        try:
#            if self.passtable.loc[website] == [login, password]:
#                self.passtable.loc[website+'1'] = [login, password]
#            else:
#                df.loc[website] = [login, password]
#        except:
#            df.loc[website] = [login, password]

    def del_entry(self, website):
       self.passtable.drop(website, axis = "index", inplace = True) 
       print("success")

    """workign on a clear table entry to delete the entire dataframe"""
#    def clear_table(self):
