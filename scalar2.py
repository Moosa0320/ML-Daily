import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

X = np.array([[2500,1],[2548,3],[2987,5]])

print("Orginal values are :", X)

sScalar = StandardScaler()
sScaledValue = sScalar.fit_transform(X)

mScalar = MinMaxScaler()
mScaledValue = mScalar.fit_transform(X)

print("Scaled by Standard :", sScaledValue)
print("Scaled by Min Max :", mScaledValue)

