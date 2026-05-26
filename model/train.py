from pathlib import Path
from preprocessing.text_parser import read_text
from preprocessing.text_parser import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# 1. Build dataset
X = []
y = []

p = Path(r"C:\Users\Clark\source\repos\documentClassification\data")

for subdir in p.iterdir():
    label = subdir.name

    for file in subdir.iterdir():
        text = read_text(file)
        cleaned = clean_text(text)

        X.append(cleaned)
        y.append(label)

# 2. TF-IDF
vectorizer = TfidfVectorizer()
X_vectors = vectorizer.fit_transform(X)

# 3. Train model
model = LogisticRegression()
model.fit(X_vectors, y)


import joblib

joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")