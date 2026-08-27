from sklearn.linear_model import SGDRegressor,LinearRegression
import numpy as np

X = np.random.rand(100,1)
Y = 3.5 * X.flatten() + 2.5 + np.random.randn(100)

model = LinearRegression()
model.fit(X,Y)
direct = model.coef_[0]

gmodel = SGDRegressor(learning_rate='adaptive',eta0=0.1,max_iter=1000,random_state=42)
gmodel.fit(X,Y)
gdirect = gmodel.coef_[0]

print(f"Coef Linear {direct}")
print(f"Coef SGR {gdirect}")