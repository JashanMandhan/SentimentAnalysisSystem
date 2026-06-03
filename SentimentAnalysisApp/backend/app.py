from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Load the sentiment analysis model
model = joblib.load("model.pkl")  # You need your trained model here

@app.route('/predict', methods=['POST'])
def predict():
    # Extract text data from request
    data = request.get_json()
    text = data.get("text", "")
    
    # Predict sentiment
    prediction = model.predict([text])
    
    # Return prediction
    return jsonify({"sentiment": prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
