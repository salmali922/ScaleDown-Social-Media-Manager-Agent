def predict_engagement(post, insights):
    score = 50

    if "AI" in post:
        score += 15
    if "tips" in post.lower():
        score += 10
    if len(post) > 80:
        score += 10
    if "evening" in insights.lower():
        score += 5

    return min(score, 100)
