import streamlit as st
import pdfplumber

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file is not None:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    st.subheader("Resume Content")
    st.write(text)

    skills = ["Python", "Machine Learning", "Data Science",
              "SQL", "AI", "Pandas"]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Detected Skills")
    st.write(found_skills)

    score = len(found_skills) * 10

    st.subheader("Resume Score")
    st.write(score)