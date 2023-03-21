import numpy as np
import pandas as pd

# 1번
df_t = pd.read_csv('./HYNN/data/titanic.csv')
# print(df_t.head(5))

# pd.isnull 누락값 여부 체크
def check_missing(vec) : 
    null_vec = pd.isnull(vec)
    return null_vec

# 컬럼별로 누락값의 갯수
def count_missing(vec) : 
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count

# 컬럼별 누락의 비율
def prop_missing(vec) :
    total = count_missing(vec) # 누락 총 갯수
    rowlen = vec.size
    rst = total / rowlen
    return rst
# vx = np.NaN
# rst = check_missing(vx)
# print(rst)

# df_miss = df_t.apply(count_missing)
# print(df_miss)

df_cnt_m = df_t.apply(count_missing, axis=1) # 한 행에대해 여러개 열에 적용
# print(df_cnt_m)

df_prop_m = df_t.apply(prop_missing)
# print(df_prop_m)


df_t['num_missing'] = df_t.apply(count_missing, axis=1)
# print(df_t.head(5))

df_t_final = df_t.loc[df_t.num_missing > 1, :]
# print(df_t_final.head(5))

total = pd.DataFrame()
total['li'] = [0, 10, 2, 30, 44, 5, 22, 90]
div = 4
rst = total/div
print(rst)