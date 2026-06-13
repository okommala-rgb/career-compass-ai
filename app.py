import streamlit as st
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv
from translations import translations

# =========================
# Load Environment Variables
# =========================

load_dotenv()

try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# =========================
# Page Config
# =========================

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

st.sidebar.title("AI Settings")

ai_provider = st.sidebar.selectbox(
    "AI Provider",
    ["Gemini", "Ollama"]
)

user_api_key = st.sidebar.text_input(
    "Bring Your Own API Key",
    type="password"
)

# =========================
# Gemini Function
# =========================

def ask_gemini(prompt, api_key):
    try:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"❌ Gemini Error:\n\n{str(e)}"

# =========================
# Ollama Function
# =========================

def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]

    except Exception as e:
        return f"""
❌ Ollama Error

{str(e)}

Ollama works when running locally.

Commands:

ollama pull llama3

ollama run llama3
"""

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

            if ai_provider == "Gemini":

                api_key_to_use = (
                    user_api_key
                    if user_api_key
                    else GEMINI_API_KEY
                )

                if not api_key_to_use:
                    st.error(
                        "Please enter your Gemini API Key or configure a default key."
                    )

                else:

                    report = ask_gemini(
                        prompt,
                        api_key_to_use
                    )

                    st.success(
                        "Gemini AI Career Report Generated"
                    )

                    st.markdown(report)

            else:

                report = ask_ollama(prompt)

                st.success(
                    "Ollama AI Career Report Generated"
                )

                st.markdown(report)