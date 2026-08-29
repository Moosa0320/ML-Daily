import numpy as np 
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

vector = CountVectorizer()
messages = ["Hello! You won","Lottery Tickey","Meeting at 6.00","Email from Google"]
flags = ["spam","spam","not spam","not spam"]

X_train = vector.fit_transform(messages)

model = LogisticRegression()
model.fit(X_train,flags)


testMessage = ["Urgent Meeting"]
X_test = vector.transform(testMessage)

prediction = model.predict(X_test)
predictProb = model.predict_proba(X_test)

print("Prediction", prediction)
print("Prob", predictProb)