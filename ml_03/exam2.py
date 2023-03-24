import pandas as pd
from datetime import datetime 

df = pd.read_csv('./HYNN/data/COVID19.csv')
# print(df)

df['시점'] = pd.to_datetime(df['시점'])
print(df['시점'])
