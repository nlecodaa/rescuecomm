import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("train.csv")

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)
print("✅ Model trained successfully!")

acc = model.score(X_test, y_test)
print(f"Test accuracy: {acc*100:.2f}%")

joblib.dump(model, "rescuecomm_clf.pkl")
print("💾 Model saved to rescuecomm_clf.pkl")
