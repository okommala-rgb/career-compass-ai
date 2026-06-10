import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-1.5-flash")

# Page config
st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🎯",
    layout="wide"
)

# Title
st.title("🎯 Career Compass AI")
st.subheader("Find Your Direction. Build Your Future.")

st.markdown("---")

# Inputs
name = st.text_input("Your Name")

skills = st.text_area(
    "Your Skills",
    placeholder="Python, Machine Learning, Communication, DSA..."
)

interests = st.text_area(
    "Your Interests",
    placeholder="AI, Startups, Robotics, Design..."
)

dream = st.text_input(
    "Dream Career",
    placeholder="AI Engineer"
)

# Button
if st.button("Generate Career Report"):

    if not name or not skills or not interests or not dream:
        st.warning("Please fill all fields.")
    else:

        prompt = f"""
        Student Name: {name}

        Skills:
        {skills}

        Interests:
        {interests}

        Dream Career:
        {dream}

        Act as a professional career counselor.

        Create a detailed personalized career report.

        Include:

        1. Career Analysis
        2. Strengths
        3. Skills to Improve
        4. Learning Roadmap
        5. Recommended Certifications
        6. Future Job Opportunities
        7. Salary Expectations
        8. Final Motivation

        Format beautifully using markdown.
        """

        with st.spinner("Analyzing your profile..."):

            response = model.generate_content(prompt)

            st.success("Career Report Generated Successfully!")

            st.markdown(response.text)