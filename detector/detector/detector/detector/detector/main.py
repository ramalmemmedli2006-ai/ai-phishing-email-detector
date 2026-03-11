from pathlib import Path

from detector.predictor import predict_email
from detector.preprocess import clean_text
from detector.rules import calculate_rule_score, get_rule_verdict


MODEL_PATH = Path("model/phishing_model.pkl")


def print_banner() -> None:
    print("=" * 55)
    print("         AI-POWERED PHISHING EMAIL DETECTOR")
    print("=" * 55)


def explain_result(ai_result: dict, rule_score: int, rule_verdict: str) -> None:
    print("\n=== Analysis Result ===")
    print(f"AI Prediction: {ai_result['label']}")

    if "phishing_probability" in ai_result:
        probability = ai_result["phishing_probability"] * 100
        print(f"Phishing Probability: {probability:.2f}%")

    print(f"Rule-Based Risk Score: {rule_score}/100")
    print(f"Rule Verdict: {rule_verdict}")

    final_verdict = "Phishing" if ai_result["prediction"] == 1 or rule_score >= 70 else "Likely Legitimate"
    print(f"Final Verdict: {final_verdict}")


def main() -> None:
    print_banner()

    if not MODEL_PATH.exists():
        print("Model not found. Please run: python train_model.py")
        return

    email_text = input("\nPaste the email content:\n> ").strip()

    if not email_text:
        print("No email content provided.")
        return

    cleaned = clean_text(email_text)
    ai_result = predict_email(cleaned)
    rule_score = calculate_rule_score(email_text)
    rule_verdict = get_rule_verdict(rule_score)

    explain_result(ai_result, rule_score, rule_verdict)


if __name__ == "__main__":
    main()
