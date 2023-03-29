import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

iris_data = iris.data
# print(iris_data)
iris_label = iris.target
# print(iris_label)
iris_feature = iris.feature_names
# print(iris_feature)

iris_df = pd.DataFrame(data=iris_data, columns=iris_feature)
iris_df['label'] = iris_label
# print(iris_df)

x_train, x_test, y_train, y_test = train_test_split(
    iris['data'], iris['target'], random_state=11, test_size=0.2)
print(x_train.shape)
print(x_test.shape)

# 트레이닝 데이터로 학습하기
# decision_tree = DecisionTreeClassifier(random_state=40)
# 26을 수정
decision_tree = DecisionTreeClassifier(max_depth=3, random_state=40)
decision_tree.fit(x_train, y_train)

# 랜덤하게 샘플 데이터를 넣어서 예측
x_new = np.array([[7.1, 2.2, 6.8, 0.4]])
prediction = decision_tree.predict(x_new)
# print(prediction)
print('예측 결과 :', iris['target_names'][prediction])

print(decision_tree.score(x_test, y_test))

# 가지치기 line26 수정
