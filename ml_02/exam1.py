import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# iris data에서
# apply & count_missing 함수를 사용해서
# 결측값이 몇개 있는지 체크

iris = load_iris()

df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

def count_missing(n) : 
    temp = pd.isna(n)
    result = np.sum(temp)
    return result
print('결측값의 수\n{}'.format(df_iris.apply(count_missing)))

# sepal 길이 컬럼만 반올림해서 새로운 sepal_new 컬럼으로 추가
df_iris['sepal_new'] = round(df_iris['sepal length (cm)']) 
print(df_iris)



