from datetime import datetime
import pandas as pd

df_time = pd.read_csv('./HYNN/data/country_timeseries.csv', parse_dates=['Date'])

df_time['yyyy'] = df_time['Date'].dt.year
df_time['mm'] = df_time['Date'].dt.month
print(df_time[['yyyy', 'mm']].head(5))