import sys

import joblib
from preprocessing.text_parser import read_text, clean_text
from pathlib import Path

# load model + vectorizer
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# file to test
#file_path = Path(r"C:\Users\Clark\source\repos\documentClassification\data\support_tickets\ticket1.txt")
file_path = Path(sys.argv[1])

# preprocess
text = read_text(file_path)
cleaned = clean_text(text)

# vectorize
X_input = vectorizer.transform([cleaned])

# predict
prediction = model.predict(X_input)
probs = model.predict_proba(X_input)

confidence = max(probs[0])

print("Predicted label:", prediction[0])
print("Confidence:", confidence)