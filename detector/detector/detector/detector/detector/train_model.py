from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from detector.preprocess import clean_text


DATA_PATH = "data/sample_emails.csv"
MODEL_DIR = Path("model")
MODEL_PATH = MODEL_DIR / "phishing_model.pkl"


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    df["clean_text"] = df["text"].astype(str).apply(clean_text)

    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), stop_words="english")),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(df["clean_text"], df["label"])

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"Model trained and saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
