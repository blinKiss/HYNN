import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A' : [3,3], 'B' : [8,9], 'C' : [9,3],
    'D' : [4,7], 'E' : [1,6], 'F' : [5,2],
    'G' : [7,2], 'H' : [2,10], 'I' : [4,5]
})

X1 = np.random.randint(10, size=2)
X2 = np.random.randint(10, size=2)

def N_dist(dat, No):
    dat.loc['N_far'] = 0.0
    for i in range(len(dat.columns)):
        dat.loc['N_far'][i] = round( ( ((dat.loc[0][i] - No[0])**2) + ((dat.loc[1][i] - No[1])**2))**(1/2), 2 )
    return '가장 가까운 점 : {}{}, 거리 : {}'.format(dat.loc['N_far'].idxmin(),
                                           tuple(df['{}'.format(dat.loc['N_far'].idxmin())].iloc[:-1].values.astype(int)),
                                           dat.loc['N_far'].min()) 

print('X1{}과 {}\nX2{}와 {}'.format(tuple(X1), N_dist(df, X1), tuple(X2), N_dist(df, X2)))
