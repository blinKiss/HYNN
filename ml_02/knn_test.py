import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
# print(iris)

iris_data = iris.data
col_name = iris.feature_names

iris_df = pd.DataFrame(data=iris_data, columns=col_name)
# print(iris_df)
# print(iris.target)

# train_test_split 함수제공 (분리하고 섞어줌)
X_train, X_test, Y_train, Y_test = train_test_split(iris['data'], iris['target'], random_state=0)
# print('X_train 행의 크기 : {}'.format(X_train.shape))
# print('X_test 열의 크기 : {}'.format(X_test.shape))

# print('Y_train 행의 크기 : {}'.format(Y_train.shape))
# print('Y_train 열의 크기 : {}'.format(Y_test.shape))

knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, Y_train) # train 데이터

# 샘플 임의 데이터
# 데이터는 리스트 복수로 들어감
X_new = np.array([[6, 2.1, 4.1, 0.3]]) # 꽃받침 길이, 너비, 꽃잎 길이, 너비
pre_result = knn.predict(X_new)

print('예측된 결과 : {} -> {}'.format(pre_result, iris['target_names'][pre_result]))



