import numpy as np

w = np.array([10.0,5.0,-0.5])
d = np.array([2.0,-1.0,3.0])
alpha = 0.1

w = w - (alpha * d)
print(w)