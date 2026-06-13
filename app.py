import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from translations import translations

# Load .env for local development
load_dotenv()

# Gemini API Key
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🎯",
    layout="wide"
)

# =========================
# Sidebar
# =========================

language = st.sidebar.selectbox(
    "Language",
    ["English", "తెలుగు"]
)

t = translations[language]

st.sidebar.title("Career Compass AI")
st.sidebar.success("Powered by Gemini AI")

# =========================
# Gemini Function
# =========================

def ask_gemini(prompt):
    try:
        genai.configure(api_key=GEMINI_API_KEY)

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"❌ Gemini Error:\n\n{str(e)}"

# =========================
# Main UI
# =========================

st.title(t["title"])
st.subheader(t["subtitle"])

st.markdown("---")

name = st.text_input(t["name"])

skills = st.text_area(
    t["skills"],
    placeholder="Python, Machine Learning, Communication, DSA..."
)

interests = st.text_area(
    t["interests"],
    placeholder="AI, Startups, Robotics, Design..."
)

dream = st.text_input(
    t["dream"],
    placeholder="AI Engineer"
)

if st.button(t["button"]):

    if not skills or not dream:
        st.warning(
            "Please enter your skills and dream career."
        )

    elif not GEMINI_API_KEY:
        st.error(
            "Gemini API Key not configured."
        )

    else:

        prompt = f"""
You are an expert AI Career Counselor.

Student Name:
{name}

Skills:
{skills}

Interests:
{interests}

Dream Career:
{dream}

Generate a professional report with:

# Career Analysis

# Skill Gap Analysis

# Learning Roadmap
(3 Month Plan)

# Suitable Job Roles

# Recommended Certifications

# Salary Outlook

# Projects To Build

# Final Recommendation

Use bullet points and proper formatting.
"""

        with st.spinner("Generating Career Report..."):

            report = ask_gemini(prompt)

            st.success(
                "Career Report Generated Successfully"
            )

            st.markdown(report)