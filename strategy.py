def generate_strategy(metrics):
    if not metrics:
        return "No data available."

    if metrics["best_platform"] == "Instagram":
        return "Focus on short-form reels."
    elif metrics["best_platform"] == "LinkedIn":
        return "Prioritize professional content."
    else:
        return "Diversify content formats."
