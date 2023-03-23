import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터프레임을 가져와서 성적의 평균 막대그래프를 그리시오
import oracledb

conn = oracledb.connect(user='jsp4', password='123456', dsn='localhost:1521/doremiplay')
curs = conn.cursor()

sql = "SELECT * FROM stu_test1"
curs.execute(sql)

out_data = curs.fetchall()

df = pd.DataFrame(out_data)
df.columns = ['번호', '이름', 'Python 점수', 'Spark 점수', 'R 점수']
# df2 = df.iloc[0:, 2:5]
print(df)


x = np.arange(len(df['이름']))
y = df['Python 점수']
name = df['이름']
fig = plt.figure()
sub1 = fig.add_subplot(1,2,1)
sub2 = fig.add_subplot(1,2,2)

sub1.bar(x - 0.2, y, width = 0.2, label = 'Python', color='skyblue')
sub1.bar(x, df['Spark 점수'], width = 0.2, label = 'Spark', color='blueviolet')
sub1.bar(x + 0.2, df['R 점수'], width = 0.2, label = 'R', color='orchid')

# 총합 평균 막대그래프로
df2 = df.drop(['이름'], axis=1)
sum = df2.sum(axis=1)
avg = df2.mean(axis=1)
sub2.bar(x - 0.15, sum, width = 0.3, label = '총점', color='purple')
sub2.bar(x + 0.15, avg, width = 0.3, label = '평균', color='violet')

sub1.set_xticks(x, name)
sub2.set_xticks(x, name)
sub1.legend()
sub2.legend()
plt.show()
