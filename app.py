import streamlit as st
from compressor import compress_context
from agent import generate_post, adapt_post
from scheduler import schedule_post
from viral_score import predict_viral_score
import database
import sqlite3
import pandas as pd
from agent import generate_post, generate_caption, predict_engagement, adapt_post, generate_weekly_calendar, generate_strategy, generate_monthly_calendar



st.set_page_config(page_title="Autonomous Social AI Agent")

st.title("🤖 Autonomous Social Media Manager (Powered by ScaleDown)")


history = st.text_area("Paste past content/history")

if st.button("Analyze Audience"):
    insights = compress_context(history)
    st.session_state.insights = insights
    st.success("Insights extracted!")

if "insights" in st.session_state:

   if st.button("Generate Post"):
    post = generate_post(st.session_state.insights)
    caption = generate_caption(post)

    st.session_state.post = post
    st.session_state.caption = caption

    st.write("Generated Post:")
    st.write(post)

    st.write("Caption:")
    st.write(caption)



platforms = st.multiselect(
    "Select Platforms",
    ["Instagram", "LinkedIn", "X", "YouTube"]
)

time = st.text_input("Schedule Time")

if st.button("Predict Engagement"):
    score = predict_engagement(st.session_state.post)
    st.session_state.score = score
    st.write(f"🔥 Viral Score: {score}%")


if st.button("Schedule Post"):
    adapted_posts = []
    for p in platforms:
        adapted = adapt_post(st.session_state.post, p)
        adapted_posts.append(adapted)

    schedule_post(
    "\n---\n".join(adapted_posts) +
    "\n\nCaption:\n" +
    st.session_state.caption,

        ",".join(platforms),
        time,
        st.session_state.get("score", 80)
    )

    st.success("Post scheduled successfully!")
st.subheader("📊 Scheduled Posts Analytics")

conn = sqlite3.connect("posts.db")
df = pd.read_sql("SELECT * FROM posts", conn)

if not df.empty:

    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df = df.dropna(subset=["score"])

    st.dataframe(df)

    st.subheader("🔥 Engagement Trend")
    st.line_chart(df["score"])

    st.subheader("📱 Platform Comparison")
    platform_avg = df.groupby("platform")["score"].mean()
    st.bar_chart(platform_avg)

else:
    st.write("No posts scheduled yet.")


# Split platforms stored as comma-separated values
platform_data = []

for _, row in df.iterrows():
    platforms = row["platform"].split(",")
    for p in platforms:
        platform_data.append({
            "platform": p.strip(),
            "score": row["score"]
        })

platform_df = pd.DataFrame(platform_data)

if not platform_df.empty:
    avg_scores = platform_df.groupby("platform")["score"].mean()
    st.bar_chart(avg_scores)


else:
    st.write("No posts scheduled yet.")
st.subheader("🗓 Weekly Content Planner")

try:
   df["time"] = pd.to_datetime(df["time"], errors="coerce", utc=True)

   df["day"] = df["time"].dt.day_name()
   posts_per_day = df.groupby("day").size()
   st.bar_chart(posts_per_day)

except:
    st.write("Time format not recognized for weekly chart.")
st.subheader("🗓 Auto Weekly Content Calendar")

if st.button("Generate Weekly Plan"):
    weekly_plan = generate_weekly_calendar(
        st.session_state.get("insights", "")
    )

    for day_plan in weekly_plan:
        st.write(day_plan)
st.subheader("📈 AI Content Strategy")

if st.button("Get Strategy Suggestions"):
    strategies = generate_strategy(
        st.session_state.get("insights", "")
    )

    for tip in strategies:
        st.write("✅", tip)
st.subheader("📅 30-Day AI Content Calendar")

if st.button("Generate 30-Day Plan"):
    monthly_plan = generate_monthly_calendar(
        st.session_state.get("insights", "")
    )

    for post in monthly_plan:
        st.write(post)
