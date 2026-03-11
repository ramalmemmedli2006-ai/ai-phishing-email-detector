import joblib


MODEL_PATH = "model/phishing_model.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def predict_email(text: str) -> dict:
    model = load_model()
    prediction = model.predict([text])[0]

    probabilities = None
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba([text])[0]

    result = {
        "prediction": int(prediction),
        "label": "Phishing" if int(prediction) == 1 else "Legitimate",
    }

    if probabilities is not None:
        result["phishing_probability"] = float(probabilities[1])

    return result
