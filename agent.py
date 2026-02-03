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
