from flask import Flask, request, jsonify
from flask_cors import CORS
from sentiment_utils import predict_sentiment  # Import function from sentiment_utils.py

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend-backend communication

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data sent by the frontend
    text = data.get("text", "")  # Extract the text field from the data

    sentiment = predict_sentiment(text)  # Predict the sentiment using sentiment_utils
    return jsonify({"sentiment": sentiment})  # Return sentiment as JSON

if __name__ == '__main__':
    app.run(debug=True)
