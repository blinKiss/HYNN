import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'fruit' : ['바나나', '바나나', '바나나', '사과', '사과', '사과', '딸기', '딸기', '딸기'],
    'date' : ['2018.1.1', '2019.4.1', '2020.7.1', '2018.1.1', '2019.4.1', '2020.7.1', '2018.1.1', '2019.4.1', '2020.7.1'],
    'price' : [3500, 3100, 4000, 5500, 7500, 6500, 12000, 11000, 13000]    
})

# date 변경
df['date'] = pd.to_datetime(df['date'])

# 연도별로 평균을 구하시오
df_y_mean = round(df.groupby(df['date'].dt.year).mean())
print(df_y_mean)
# 그래프로 그리시오
mean = df_y_mean.plot()
plt.show()

