import numpy as np
from sklearn.preprocessing import MinMaxScaler

X = np.array([[2000,3],[2340,5],[3400,7]])

print(f"Orignal",X)

scalar = MinMaxScaler()
transX = scalar.fit_transform(X)

print("Scaled", transX)