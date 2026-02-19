import pandas as pd

def compute_metrics(df):
    if df.empty:
        return None

    avg_score = df["score"].mean()
    total_posts = len(df)

    platform_avg = df.groupby("platform")["score"].mean()
    best_platform = platform_avg.idxmax()

    return {
        "total_posts": total_posts,
        "avg_score": round(avg_score, 2),
        "best_platform": best_platform,
        "platform_avg": platform_avg
    }
