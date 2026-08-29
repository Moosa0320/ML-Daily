import numpy as np
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression


X = np.array([3200,4000,5300,3400,5400]).reshape(-1,1)
Y = np.array([200,300,560,240,510,550])

poly = PolynomialFeatures(degree=2,include_bias=False)
X_poly = poly.fit_transform(X)

print("Tranformed size in :",X_poly)

scaling = StandardScaler()
X_scaled = scaling.fit_transform(X_poly)

print("Scaled X Feature :",X_scaled)

model = LinearRegression()
model.fit(X_scaled,Y)

prediction = model.predict(X_scaled)
print("Prediction:",prediction)