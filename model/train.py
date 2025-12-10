import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("../dataset/fir_dataset_1000.csv")


X_train, X_test, y_train, y_test = train_test_split(df["text"], df["crime"], test_size=0.2)

model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)
joblib.dump(model, "crime_classifier.pkl")
print("Model trained and saved!")
