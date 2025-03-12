import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB

# Load the dataset
df = pd.read_csv("music_sentiment_dataset.csv")

# Rename 'User_Text' as 'Lyrics' (for compatibility)
df.rename(columns={"User_Text": "Lyrics"}, inplace=True)

# Ensure required columns exist
if "Lyrics" not in df.columns or "Sentiment_Label" not in df.columns:
    raise ValueError("Dataset must contain 'Lyrics' (User_Text) and 'Sentiment_Label' columns.")

# Convert text data into numerical format using TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df["Lyrics"])

# Encode sentiment labels
encoder = LabelEncoder()
y = encoder.fit_transform(df["Sentiment_Label"])

# Train a basic Naive Bayes classifier
model = MultinomialNB()
model.fit(X, y)

# Save the model, TF-IDF vectorizer, and encoder
joblib.dump(model, "model.pkl")
joblib.dump(tfidf, "tfidf.pkl")
joblib.dump(encoder, "encoder.pkl")

print("✅ Model training complete! Saved model.pkl, tfidf.pkl, and encoder.pkl.")

