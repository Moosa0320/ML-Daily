from sklearn.linear_model import LogisticRegression
import numpy as np

probabilities = np.array([[0.1,0.4,0.6,0.9]])

defaultProbs = (probabilities >= 0.5).astype(int)
print("Default Threshold :",defaultProbs)

newProbs = (probabilities >=0.8).astype(int)
print("New Threshold :",newProbs)