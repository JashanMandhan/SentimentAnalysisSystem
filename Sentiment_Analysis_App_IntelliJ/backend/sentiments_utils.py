import joblib
import nltk
import string

# Download necessary NLTK data files
nltk.download('punkt')

# Load the trained sentiment analysis model
model = joblib.load("model.pkl")

# Preprocess text: lowercasing, removing punctuation, tokenizing
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = ''.join([char for char in text if char not in string.punctuation])  # Remove punctuation
    tokens = nltk.word_tokenize(text)  # Tokenize the text (split it into words)
    return ' '.join(tokens)  # Join tokens back into a single string

# Sentiment prediction function
def predict_sentiment(text):
    processed_text = preprocess_text(text)  # Preprocess the input text
    prediction = model.predict([processed_text])  # Predict sentiment using the model
    return prediction[0]  # Return the predicted sentiment (e.g., Positive, Negative)
