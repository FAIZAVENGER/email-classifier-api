import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib

# Load data
df = pd.read_csv("combined_emails_with_natural_pii.csv")

# Feature and label
X = df["email"]
y = df["type"]


# Pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train
pipeline.fit(X, y)

# Save model
joblib.dump(pipeline, "email_classifier_model.pkl", compress=5)


