# Sentiment Analysis System

A machine learning web application that classifies text as positive, negative, or neutral. Built with a scikit-learn NLP pipeline served via a Flask REST API and a vanilla JS frontend.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| ML / NLP | Python, scikit-learn, NLTK, joblib |
| Backend API | Flask, Flask-CORS |
| Frontend | HTML, CSS, JavaScript |
| Model | Pre-trained classifier serialised as `model.pkl` |
| Notebook | Jupyter (NLP-2.ipynb — exploratory analysis) |

## Project Structure

```
SentimentAnalysisApp/
├── backend/
│   ├── app.py              # Flask REST API
│   ├── sentiment_utils.py  # Text preprocessing and prediction helpers
│   └── model.pkl           # Trained scikit-learn model
└── frontend/
    ├── index.html          # UI
    ├── style.css
    └── app.js              # Fetch calls to backend API

NLP-2.ipynb                 # Jupyter notebook — NLP exploration
```

## Getting Started

```bash
cd SentimentAnalysisApp/backend
pip install flask flask-cors joblib scikit-learn nltk
python app.py
```

Open `frontend/index.html` in your browser.

## Author

Jashanveer Mandhan
