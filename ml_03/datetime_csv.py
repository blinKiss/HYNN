from datetime import datetime 
import pandas as pd

df_time = pd.read_csv('./HYNN/data/country_timeseries.csv', parse_dates=['Date'])
print(df_time['Date'].head(5))

# 숫자 월 -> 문자 월로 변환
# 01 -> January 형태로

df_time['dttm_1'] = df_time['Date'].dt.strftime('%Y-%B-%d')
print(df_time[['Date', 'dttm_1']])