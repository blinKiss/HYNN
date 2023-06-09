# exam6 이었다가 변경
import pandas as pd

df = pd.DataFrame({
    'weather': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy'],  # 0,1,2
    'temperature': ['hot', 'hot', 'hot', 'mild', 'cool'],  # 30, 20, 10
    'humidity': ['high', 'high', 'low', 'high', 'normal'],  # 60, 50, 40
    'windy': [False, True, False, False, False],  # 0, 1
    'basket_target': ['no', 'no', 'yes', 'yes', 'yes']  # 0, 1
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

print(df2)
