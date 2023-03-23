import numpy as np

scores = np.random.randint(0, 100, (7,3))
scores_str = np.array2string(scores, separator=',')
print(scores_str)