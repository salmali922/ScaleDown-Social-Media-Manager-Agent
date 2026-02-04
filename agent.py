import random

def generate_post(context):
    topics = [
        "Boost productivity with AI tools",
        "5 tips for better coding",
        "Daily motivation for developers",
        "Learn data science smarter",
        "Future of AI careers"
    ]

    if context:
        return f"{random.choice(topics)} based on audience interest."
    return random.choice(topics)


def generate_caption(post):
    captions = [
        f"🚀 Ready to level up? {post}",
        f"Start improving today: {post}",
        f"Small steps lead to big success — {post}",
        f"Consistency wins. {post}"
    ]

    hashtags = "#AI #Tech #Learning #Growth"

    return random.choice(captions) + "\n\n" + hashtags


def predict_engagement(post):
    base = 70
    bonus = min(len(post) // 10, 20)
    return base + bonus


def adapt_post(post, platform):
    return post + f"\nOptimized for {platform}"
def generate_weekly_calendar(context):
    topics = [
        "AI productivity tips",
        "Coding tutorial",
        "Career motivation",
        "Tech industry trends",
        "Learning resources",
        "Developer tips",
        "Future tech discussion"
    ]

    calendar = []
    for i, topic in enumerate(topics):
        calendar.append(f"Day {i+1}: Post about {topic}")

    return calendar
def generate_strategy(context):
    suggestions = [
        "Post tutorials during evening peak engagement.",
        "Focus on reels and short videos.",
        "Increase motivational content mid-week.",
        "Use AI tool recommendations for higher clicks.",
        "Post career tips on weekends."
    ]

    return suggestions
def generate_monthly_calendar(context):
    themes = [
        "AI productivity",
        "Coding tutorials",
        "Career advice",
        "Tech trends",
        "Learning tips",
        "Developer motivation",
        "Startup insights",
        "AI tools",
        "Programming hacks",
        "Industry news"
    ]

    calendar = []

    for day in range(30):
        topic = themes[day % len(themes)]
        calendar.append(f"Day {day+1}: Post about {topic}")

    return calendar
