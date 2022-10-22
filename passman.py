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

    def save_db(self, df):
        df.to_csv(self.password_file)
        print('success')
    
    #def inc_dig(dig):
    def check_entry(self, web, entry, mode : Optional[str]="unmatch"):
        if web in self.passtable.index:
            print('bitch')
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
        
    def add_entry(self, website, login, password):
        entry = [login, password]
        df = self.passtable
        #print(df.loc[website][["Login","Password"]] )
        #df.loc[website] = [login, password]
        if self.check_entry(website, entry):
            if self.check_entry(website, entry, mode = "match"):
                print('Entry is already added')
            elif not self.check_entry(website+"1", entry, mode = "match"):
                """ovverride needed here define override function tomorrow"""
                df.loc[website + str(int(website[-1])+1)] = entry
                print("you're gay")
            else:
                df.loc[website+'1'] = entry
        else:
            df.loc[website] = entry
#        try:
#            if df.loc[website] == [login, password]:
#                df.loc[website+'1'] = [login, password]
#            else:
#                df.loc[website] = [login, password]
#        except:
#            df.loc[website] = [login, password]
        self.passtable = df
        self.save_db(df)

    def del_entry(self, website):
       self.passtable.drop(website, axis = "index", inplace = True) 
       self.save_db(self.passtable)
       print("success")
