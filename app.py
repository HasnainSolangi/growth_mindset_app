import streamlit as st
import random

# 🌱 List of Growth Mindset Challenges
challenges = [
    "🚀 Try learning something new today and reflect on it.",
    "🔄 Turn a failure into a lesson – what did you learn?",
    "💡 Give positive feedback to someone and uplift their day.",
    "🔥 Step outside your comfort zone in one small way.",
    "🌟 List 3 things you're grateful for and why."
]

# 📜 List of Motivational Quotes
quotes = [
    "🎯 Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "🧠 Growth happens outside your comfort zone.",
    "💪 Believe in your ability to improve, and you will.",
    "🌱 Mistakes are proof that you are trying.",
    "🚀 Your mindset is your superpower—use it wisely."
]

# 🎨 Streamlit Page Configuration
st.set_page_config(page_title="Growth Mindset App", page_icon="🌱", layout="centered")

# 🏆 Title & Intro
st.title("🌱 Growth Mindset Challenge")
st.write("#### Develop a growth mindset with daily challenges & motivation! 🌟")

# 🎯 Display a Random Challenge
st.subheader("💪 Today's Challenge:")
st.success(random.choice(challenges))

# ❤️ Display a Motivational Quote
st.subheader("📢 Motivational Quote:")
st.info(random.choice(quotes))

# ✍️ User Reflection Section
st.subheader("☄ Your Reflection:")
user_reflection = st.text_area("💡 How did you approach today's challenge?")
if user_reflection:
    st.success("⭐ Reflection saved! Keep pushing forward to your goals. 🚀")
else:
    st.warning("💭 Take a moment to reflect and share your thoughts!")

# 🎉 Celebrate Achievements
st.subheader("🎊 Celebrate Wins!")
achievement = st.text_input("🌷 Share something you've recently accomplished:")

if st.button("Submit 🎉"):
    if achievement:
        st.balloons()
        st.success(f"🎉 Amazing! Keep achieving, keep growing. 💪")
    else:
        st.error("Oops! Please enter an achievement before submitting. 🚀")

# 📌 Footer
st.markdown("---")
st.write("🌟 Keep believing in yourself. Growth is a journey, not a destination. 🚀")
st.write("### ✨ Created by **Hasnain Ahmed** ✨")
