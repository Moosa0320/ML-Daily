from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# 1. Real-world jaisa thora zyada data banate hain
# Farz karein 1000 gharon ka data hai
X = np.random.rand(1000, 1) * 10  # Ghar ka size
y = 3.5 * X.flatten() + 2 + np.random.randn(1000) # Asli Qeemat (isme thora noise/kachra bhi hai)

# 2. Gradient Descent ka Model banaya!
# max_iter = 1000 (Matlab pahari se neechay utarne ke liye maximum 1000 qadam/steps lo)
gd_model = SGDRegressor(max_iter=1000, tol=1e-3, random_state=42)

# 3. Model Train Kiya (Yeh background mein baby steps le raha hai)
gd_model.fit(X, y)

# 4. Results dekhte hain
print(f"Gradient Descent ne dhoonda Best w (Slope): {gd_model.coef_[0]}")
print(f"Gradient Descent ne dhoonda Best b (Intercept): {gd_model.intercept_[0]}")

# 5. Cost check karte hain
y_hat = gd_model.predict(X)
print(f"Predicted Value {y_hat}")
cost = mean_squared_error(y, y_hat)
print(f"Final Cost (Galti): {cost}")

