import pandas as pd
import numpy as np
import math

a = [2,3]
b = [8,9]
x = [4,8]

# 두 점의 거리공식을 사용하는 점이 많다면 함수로 정의하면 효율적
def distance(Lst1, Lst2) :
    rst = math.sqrt(math.pow( (Lst1[0]-Lst2[0]), 2)
                    + math.pow( (Lst1[1]-Lst2[1]), 2)
                    )
    return rst
ax = distance(a, x)
bx = distance(b, x)


if(ax > bx) : 
    print('b점과 가까움')
elif(ax < bx) :
    print('a점과 가까움')
else:
    print('동일함')