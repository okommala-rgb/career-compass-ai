import streamlit as st
import requests
from translations import translations

st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🎯",
    layout="wide"
)

# Sidebar

language = st.sidebar.selectbox(
    "Language",
    ["English", "తెలుగు"]
)

t = translations[language]

st.sidebar.title("AI Settings")

ai_provider = st.sidebar.selectbox(
    "AI Provider",
    ["Built-In", "Ollama"]
)

user_api_key = st.sidebar.text_input(
    "Bring Your Own API Key",
    type="password"
)

if user_api_key:
    st.sidebar.success("API Key Added")


# Ollama Function

def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception:
        return """
        ❌ Ollama is not running.

        Please install Ollama and run:

        ollama pull llama3

        then

        ollama run llama3
        """


# Main UI

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
        st.warning("Please enter your skills and dream career.")

    else:

        if ai_provider == "Ollama":

            prompt = f"""
            Name: {name}

            Skills:
            {skills}

            Interests:
            {interests}

            Dream Career:
            {dream}

            Generate:
            1. Career Analysis
            2. Skill Gap Analysis
            3. Learning Roadmap
            4. Suitable Job Roles
            5. Certifications
            6. Salary Outlook
            7. Final Recommendation
            """

            report = ask_ollama(prompt)

            st.success("AI Career Report Generated")
            st.markdown(report)

        else:

            st.success("Career Report Generated Successfully!")

            st.markdown(f"""
# 👋 Hello {name}!

## 🎯 Career Analysis
Your interest in **{dream}** aligns well with your skills and interests.

### Skills
{skills}

### Interests
{interests}

---

## 📊 Skill Gap Analysis

### Current Strengths
- Strong interest in the field
- Relevant foundational skills
- Motivation to learn

### Areas to Improve
- Advanced domain knowledge
- Real-world projects
- Communication and teamwork

---

## 🛣️ Learning Roadmap

### Next 30 Days
- Learn fundamentals
- Complete one mini project

### Next 3 Months
- Complete online courses
- Build portfolio projects

### Next 6 Months
- Earn certifications
- Participate in competitions

### Next 1 Year
- Apply for internships
- Build advanced projects

---

## 💼 Suitable Job Roles

- {dream}
- Associate {dream}
- Specialist
- Consultant

---

## 🏆 Recommended Certifications

- Google Certifications
- AWS Certifications
- Microsoft Learn
- Coursera Professional Certificates

---

## 💰 Salary Outlook

### Fresher
₹4–8 LPA

### 3 Years Experience
₹10–18 LPA

### 5 Years Experience
₹18–30 LPA

---

## ⭐ Final Recommendation

Stay consistent, keep learning, and build practical projects related to **{dream}**.
""")