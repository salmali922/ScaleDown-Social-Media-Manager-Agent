import streamlit as st
from compressor import compress_context
from agent import generate_post, adapt_post
from scheduler import schedule_post
from viral_score import predict_viral_score
import database
import sqlite3
import pandas as pd
from agent import generate_post, generate_caption, predict_engagement, adapt_post


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
    st.dataframe(df)
else:
    st.write("No posts scheduled yet.")