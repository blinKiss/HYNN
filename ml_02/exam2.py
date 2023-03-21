import numpy as np
import pandas as pd

df_score = pd.DataFrame({
    'class' : [1, 2, 3, 4, 5],
    'eng' : [90, 80, 85, 95, 75],
    'fre' : [70, 60, 80, 70, 90],
    'jpn' : [100, 90, 80, 90, 100]
})

# apply 메소드와 np.sum 을 같이 적용해서
# 각 반의 합계점수를 구하시오 total_class
# 각 과목별로 합계점수를 구하시오 total_subject

def score_sum(n) : 
    result = np.sum(n)
    return result

# temp = df_score[['eng', 'fre', 'jpn']]
# total_class = temp.apply(score_sum, axis=1)
# print(total_class)

# total_subject = temp.apply(score_sum, axis=0)
# print(total_subject)

df2 = df_score.set_index(keys='class')
df2['tot_cla'] = df2.apply(score_sum, axis=1)
df2.loc['tot_sub'] = df2.apply(score_sum, axis=0)
# df2.loc['t_sub']['t_class'] = 0
# df2 = df2.replace(0, np.NaN)
print(df2)