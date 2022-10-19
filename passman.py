import pandas as pd
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
    
    def add_entry(self, website, login, password):
        epass = password
        elog = login
        df = self.passtable
        df.loc[website] = [login, password]
#        try:
#            print(df.loc[website])
#        except:
#            df.loc[website] = [login, password]
#        else:
#            if df.loc[website] == [login, password]:
#                df.loc[website+'1'] = [login, password]
#            else:
#                df.loc[website] = [login, password]
        self.save_db(df)
