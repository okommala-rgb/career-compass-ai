import streamlit as st

st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Career Compass AI")
st.subheader("Find Your Direction. Build Your Future.")

st.markdown("---")

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

if st.button("Generate Career Report"):

    if not skills or not dream:
        st.warning("Please enter your skills and dream career.")
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