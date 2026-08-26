import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Data tayyar kiya
X = np.array([[1], [2], [3]])  # Sklearn ke liye 2D array
y = np.array([1, 2, 3])        # Asli qeemat

# ==========================================
# Hissa 1: Library (Sklearn) se Best 'w' nikala
# ==========================================
model = LinearRegression(fit_intercept=False)
model.fit(X, y)
best_w = model.coef_[0]  # Library ka best w
min_cost = mean_squared_error(y, model.predict(X)) # Library ki sab se kam cost

print(f"Library ne dhoonda Best w: {best_w}")
print(f"Sab se kam Cost: {min_cost}")

# ==========================================
# Hissa 2: U-Shape banane ki tayyari
# ==========================================
w_values = np.linspace(-0.5, 2.5, 50) # -0.5 se 2.5 tak bohat sari values
costs = []

for w in w_values:
    # Har w ki value par prediction aur cost (MSE) check karte hain
    y_hat_temp = w * X.flatten() 
    cost_temp = mean_squared_error(y, y_hat_temp)
    costs.append(cost_temp)

# ==========================================
# Hissa 3: Graph (Visualization) Banate hain!
# ==========================================
plt.figure(figsize=(8,5))

# U-Shape Line plot ki (Neeli line)
plt.plot(w_values, costs, color='blue', label='Cost Function J(w) (U-Shape)')

# Library wala answer plot kiya (Laal Star)
plt.scatter(best_w, min_cost, color='red', marker='*', s=300, label='Library ka Best "w"', zorder=5)

plt.title("Library ne U-Shape ke Bottom ko hit kiya!")
plt.xlabel("Parameter (w)")
plt.ylabel("Cost / Error (J)")
plt.legend()
plt.grid(True)
plt.show()