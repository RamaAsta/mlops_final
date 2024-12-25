from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)