import streamlit as st

st.title("Recruiter AI Agent")

resume = st.text_area("Paste Resume")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    score = 0
    
    skills = ["python", "data analysis", "machine learning"]
    
    for skill in skills:
        if skill in resume.lower() and skill in job_desc.lower():
            score += 1

    st.write("Match Score:", score)
    
    if score >= 2:
        st.success("Good Candidate")
    else:
        st.warning("Not a strong match")