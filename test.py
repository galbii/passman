import pandas as pd

df = pd.DataFrame(['hi', 'welcome', 'to', 'the', 'bonezone'])
index = ['ya', 'yeet', 'welcome', 'bitch', 'nahhhh']
df.index = index
df['hii'] = ['nani','ya', 'yeet', 'welcome', 'yet' 'hi']
#print(df.head())
#print(type(df.loc['yeet'].item))
entry = pd.Series({0: 'hi',
                   'hii':'nani'}, index = [0, 'hii'])
print(entry)
print(df.loc['ya', 'hii'] == entry['hii'])
yeet = df.loc['ya']
if yeet['hii'] == entry['hii']:
    print('hi')
print(type(df.loc['ya']) == ['hi', 'nani']) 
print(type(df.index))
