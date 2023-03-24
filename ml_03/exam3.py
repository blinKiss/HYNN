# 2번에서 가져온 datetime 데이터에서
# 월 데이터가 05인 데이터만 가져와서 출력하시오
import pandas as pd
from datetime import datetime 

df = pd.read_csv('./HYNN/data/COVID19.csv').dropna(axis=1)
# print(df.count())
# print(df['Unnamed: 4'].isna().count())

df2 = df[df['시점'].str.contains(' 05.')]
print(df2.head(7))

df['시점'] = pd.to_datetime(df['시점'])
df3 = df[df['시점'].dt.month == 5]
print(df3.head(7))
