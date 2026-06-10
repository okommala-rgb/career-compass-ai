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

        st.markdown("---")

        st.markdown(f"""
# 👋 Hello {name}!

## 🎯 Career Analysis
Your interest in **{dream}** aligns well with your skills and interests. With consistent effort and practical experience, you can successfully achieve this career goal.

---

## 📊 Skill Gap Analysis

### Current Strengths
- {skills}

### Areas to Improve
- Advanced technical knowledge
- Industry-level projects
- Communication and teamwork
- Problem-solving skills

---

## 🛣️ Learning Roadmap

### 📅 Next 30 Days
- Learn core concepts
- Complete one mini project
- Build a study schedule

### 📅 Next 3 Months
- Complete online courses
- Build 2 portfolio projects
- Improve problem-solving skills

### 📅 Next 6 Months
- Earn certifications
- Participate in hackathons
- Create a strong LinkedIn profile

### 📅 Next 1 Year
- Apply for internships
- Build advanced projects
- Prepare for interviews

---

## 💼 Suitable Job Roles

- {dream}
- Associate {dream}
- Analyst
- Consultant
- Specialist

---

## 🏆 Recommended Certifications

- Google Career Certificates
- AWS Certifications
- Microsoft Learn Certifications
- Coursera Professional Certificates

---

## 🚀 Project Ideas

### Beginner
Create a simple portfolio website.

### Intermediate
Build a real-world application related to your field.

### Advanced
Develop an AI-powered or industry-focused solution.

---

## 💰 Salary Outlook

### Fresher
₹4–8 LPA

### 3 Years Experience
₹10–18 LPA

### 5 Years Experience
₹18–30 LPA

---

## ⭐ Career Readiness Score

80 / 100

---

## 🎉 Final Recommendation

Focus on continuous learning, practical projects, networking, and certifications. Stay consistent and your chances of reaching your dream career will improve significantly.
""")