# exam6 이었다가 변경
import pandas as pd

df = pd.DataFrame({
    'weather': ['sunny', 'sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'sunny', 'overcast', 'rainy', 'rainy'],  # 0,1,2
    # 30, 20, 10
    'temperature': ['hot', 'cool', 'mild', 'hot', 'mild', 'cool', 'hot', 'mild', 'mild', 'cool'],
    # 60, 50, 40
    'humidity': ['high', 'normal', 'high', 'high', 'high', 'normal', 'high', 'low', 'high', 'normal'],
    # 0, 1
    'windy': [False, False, True, False, False, False, True, False, True, True],
    # 0, 1
    'basket_target': ['no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'no', 'yes']
})

# df.insert(loc=1,
#           column='weather_no',
#           value=df['weather'].replace(['sunny', 'overcast', 'rainy'], [0, 1, 2]))
# print(df)

wea_temp = {'sunny': 0, 'overcast': 1, 'rainy': 2}
tem_temp = {'hot': 30, 'mild': 20, 'cool': 10}
hum_temp = {'high': 60, 'normal': 50, 'low': 40}
win_temp = {False: 0, True: 1}
bas_temp = {'no': 0, 'yes': 1}

# 1
# df[column + '문자열'] 이런것도 되네?
# for column, temp in zip(['weather', 'temperature', 'humidity', 'windy', 'basket_target'],
#                         [wea_temp, tem_temp, hum_temp, win_temp, bas_temp]):
#     df[column + '_to_int'] = df[column].map(temp)

# print(df)

# 2
df2 = pd.DataFrame()
for column, temp in zip(['weather', 'temperature', 'humidity', 'windy', 'basket_target'],
                        [wea_temp, tem_temp, hum_temp, win_temp, bas_temp]):
    # print(type(column), type(temp))
    df2[column] = df[column].map(temp)

df3 = df2.iloc[:, 0:3]
print(df3)
