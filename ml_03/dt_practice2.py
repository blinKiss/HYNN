from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 부도난 은행 정보
df_bank = pd.read_csv('./HYNN/data/banklist.csv', parse_dates=['Closing Date', 'Updated Date'])
# print(df_bank.info())
# df_bank['close_year'] = df_bank['Closing Date'].dt.year
# print(df_bank.head(5))

# dt.quarter = 분기
df_bank['close_year'], df_bank['close_q'] = df_bank['Closing Date'].dt.year, df_bank['Closing Date'].dt.quarter
# print(df_bank[['Closing Date', 'close_year', 'close_q']])

df_bank_y = df_bank.groupby(['close_year']).size()


sub = df_bank_y.plot()
plt.show()
