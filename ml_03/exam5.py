import pandas as pd

df = pd.read_csv('./HYNN/data/titanic.csv')
df2 = df[['Survived', 'Sex', 'Age']].dropna()
# 탑승 인원
onBoard = df['Survived'].count()

# 생존 인원
df3 = df2[df2['Survived'] == 1]
survived = df3['Survived'].count()


# 생존 인원 중 남성
df_m = df3[df3['Sex'] == 'male']
df_m_cnt = df_m['Sex'].count()

# 생존 인원 중 여성
df_f = df3[df3['Sex'] == 'female']
df_f_cnt = df_f['Sex'].count()

# 생존 남성 나이별로 나눔
df_m_30u = df_m[df_m['Age'] >= 30]['Age'].count()
df_m_30d = df_m[df_m['Age'] < 30]['Age'].count()
print(df_m_30u)
# 생존 여성 나이별로 나눔
df_f_30u = df_f[df_f['Age'] >= 30]['Age'].count()
df_f_30d = df_f[df_f['Age'] < 30]['Age'].count()

print('남성의 생존 확률 : {}%, 그 중 30세 이상의 생존 확률 : {}%, 30세 미만의 생존 확률 : {}%\n'
      .format(round(df_m_cnt * 100 / survived),
              round(df_m_30u * 100 / df_m_cnt), 
              round(df_m_30d * 100 / df_m_cnt)))
print('여성의 생존 확률 : {}%, 그 중 30세 이상의 생존 확률 : {}%, 30세 미만의 생존 확률 : {}%'
      .format(round(df_f_cnt * 100 / survived),  
              round(df_f_30u * 100 / df_f_cnt), 
              round(df_f_30d * 100 / df_f_cnt)))
