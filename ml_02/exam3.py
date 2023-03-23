import pandas as pd

df = pd.DataFrame({
    'A' : [2,3],
    'B' : [8,9],
    'C' : [3,7],
    'D' : [10,2],
    'E' : [1,5],
    'F' : [6,6],
})

N = [4,8]

df.loc[2] = 0.0
for i in range(len(df.columns)):
    df.loc[2][i] = round( ( ((df.loc[0][i] - N[0])**2) + ((df.loc[1][i] - N[1])**2))**(1/2), 2 )
df = df.rename(index={0 : 'X_loc', 1 : 'Y_loc', 2 : 'N_far'})
print(df)
print('\'N\'과 가장 가까운 점은 : {}, 거리는 : {}'.format(df.loc['N_far'].idxmin(), df.loc['N_far'].min()) )