import joblib
import nltk
import string

# Download necessary NLTK data files (only once)
nltk.download('punkt')

# Load the trained model (replace 'model.pkl' with the path to your actual model file)
model = joblib.load("model.pkl")

# Function for basic text preprocessing
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    
    # Tokenize text (split text into words)
    tokens = nltk.word_tokenize(text)
    
    return ' '.join(tokens)

# Sentiment prediction function
def predict_sentiment(text):
    # Preprocess the input text
    processed_text = preprocess_text(text)
    
    # Predict sentiment using the model
    prediction = model.predict([processed_text])  # Model expects a list of text
    
    # Return the sentiment label (e.g., Positive, Negative, Neutral)
    return prediction[0]
