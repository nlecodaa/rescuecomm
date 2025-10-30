import re

KEYWORDS = {
    'fire': 40, 'flames': 40, 'explosion': 40, 'robbery': 40, 'murder': 50,
    'injured': 30, 'unconscious': 35, 'bleeding': 35, 'accident': 30,
    'argument': 10, 'noise': 5, 'fight': 20
}

def compute_risk(text):
    t = text.lower()
    score = 0
    for word, value in KEYWORDS.items():
        if word in t:
            score += value

    if 'child' in t or 'elderly' in t:
        score += 15
    if any(w in t for w in ['now', 'urgent', 'immediately']):
        score += 10

    score = max(0, min(100, score))

    if score >= 60:
        priority = "High"
    elif score >= 25:
        priority = "Medium"
    else:
        priority = "Low"

    return score, priority
