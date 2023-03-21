import numpy as np
import pandas as pd

# 간단한 함수 정의
def test_func(input) : 
    output = input*2+10
    return output


x = 5
y = test_func(x)
print(x, '->', y)

# multi_func : 숫자를 넣으면 제곱이되는 함수를 정의
def multi_func(xin):
    yout = xin ** 2
    return yout
# 50 ==> 50*50 = 2500 결과가 나오도록

yrst = multi_func(50)
print('n = {}, n^2 = {}'.format(50, yrst))