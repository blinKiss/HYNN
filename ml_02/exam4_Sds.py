import pandas as pd
import math
import numpy as np
from sklearn.neighbors import NearestNeighbors

# 세 점의 좌표를 배열로 정의합니다.
points = np.array([[8, 9], 
                   [3, 3], 
                   [9, 3], 
                   [4, 7]])

# kNN 모델을 생성합니다.
k = 1  # k=1로 설정합니다.
model = NearestNeighbors(n_neighbors=k, algorithm='kd_tree').fit(points)

# 기준점 좌표 random 
random1 = np.random.randint(10, size=2) 
random2 = np.random.randint(10, size=2)
random3 = np.random.randint(10, size=2)

# 각각의 좌표를 임의로 출력
print("random1 :", random1)
print("random2 :" ,random2)
print("random3 :" , random3)

distances1, indices1 = model.kneighbors(random1.reshape(1, -1))
distances2, indices2 = model.kneighbors(random2.reshape(1, -1))
distances3, indices3 = model.kneighbors(random3.reshape(1, -1))


# 결과를 출력
# print(random1, "에 가장 가까운 점:",  points[indices1])
print((points[indices1])  ,"이 random1인", random1,"에 가장 가까운 점입니다"  )
print((points[indices2])  ,"이 random2인", random2,"에 가장 가까운 점입니다"  )
print((points[indices3])  ,"이 random3인", random3,"에 가장 가까운 점입니다"  )
# print(random2, "random2 에 가장 가까운 점:", points[indices2])
# print(random3,"random3 에 가장 가까운 점:", points[indices3])