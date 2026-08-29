from sklearn.metrics import log_loss

y = [1,0,1]
x = [0.9,0.1,0.9]

totalCost = log_loss(y,x)

print("Tocal cost is ", totalCost)