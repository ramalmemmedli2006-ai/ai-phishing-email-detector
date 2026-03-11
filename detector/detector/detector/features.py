import re


SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "password",
    "login",
    "bank",
    "account",
    "suspended",
    "disabled",
    "confirm",
    "click",
    "prize",
    "winner",
    "invoice",
    "payment",
    "security alert",
    "credentials",
]


def extract_rule_features(text: str) -> dict:
    lowered = text.lower()

    keyword_hits = sum(1 for word in SUSPICIOUS_KEYWORDS if word in lowered)
    has_url = bool(re.search(r"http[s]?://|www\.", lowered))
    has_urgent_language = any(word in lowered for word in ["urgent", "immediately", "now", "action required"])
    asks_for_credentials = any(word in lowered for word in ["password", "login", "credentials", "verify your account"])
    mentions_money = any(word in lowered for word in ["bank", "payment", "invoice", "prize", "wallet"])

    return {
        "keyword_hits": keyword_hits,
        "has_url": has_url,
        "has_urgent_language": has_urgent_language,
        "asks_for_credentials": asks_for_credentials,
        "mentions_money": mentions_money,
    }
