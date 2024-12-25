from sklearn.metrics import classification_report
import pandas as pd
import pickle

# Load test data
data = pd.read_csv("data/heart.csv")
X_test = data.drop("target", axis=1)
y_test = data["target"]

# Load the model
model = pickle.load(open("model.pkl", "rb"))

# Evaluate the model
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)
print(report)