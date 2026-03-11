from detector.features import extract_rule_features


def calculate_rule_score(text: str) -> int:
    features = extract_rule_features(text)
    score = 0

    score += features["keyword_hits"] * 10
    score += 20 if features["has_url"] else 0
    score += 20 if features["has_urgent_language"] else 0
    score += 25 if features["asks_for_credentials"] else 0
    score += 15 if features["mentions_money"] else 0

    return min(score, 100)


def get_rule_verdict(score: int) -> str:
    if score >= 70:
        return "High Risk"
    if score >= 40:
        return "Suspicious"
    return "Low Risk"
