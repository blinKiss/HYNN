from datetime import datetime
import pandas as pd

df_time = pd.read_csv('./HYNN/data/country_timeseries.csv')
# print(df_time.iloc[-5:, :7])

df_time['date_dt'] = pd.to_datetime(df_time['Date'])
# print(df_time[['Date', 'date_dt']])
print('에볼라 바이러스\n최초 발생 시기 = {}\n최근 발생 시기 = {}'
      .format(df_time['date_dt'].min(), df_time['date_dt'].max()))

# 진행과정의 날짜 수 계산
df_time['outbreak_day'] = df_time['date_dt'] - df_time['date_dt'].min()
# print(df_time[['date_dt', 'outbreak_day']])

# 2014 데이터만 추출해서 진행날짜수를 출력하시오
df2014 = df_time[df_time['date_dt'].dt.year == 2014]
print(df2014[['date_dt', 'outbreak_day']])
