import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# Load the dataset
data = pd.read_csv(dataheart.csv)

# Preprocess data
X = data.drop(target, axis=1)
y = data[target]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Log metrics and model with MLflow
mlflow.log_param(model, RandomForest)
mlflow.log_metric(accuracy, accuracy)
mlflow.sklearn.log_model(model, model)

print(fModel trained with accuracy {accuracy.2f})