import streamlit as st
from PyPDF2 import PdfReader
import docx

st.title("Recruiter AI Agent")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

# Job description
job_desc = st.text_area("Enter Job Description")

def extract_text(file):
    if file.type == "application/pdf":
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text
        return text

def analyze(resume, job):
    skills = ["python", "data analysis", "machine learning"]
    score = sum([1 for skill in skills if skill in resume.lower() and skill in job.lower()])
    
    if score >= 2:
        return "Good Candidate", "High Rank"
    elif score == 1:
        return "Average Candidate", "Medium Rank"
    else:
        return "Not a strong match", "Low Rank"

if st.button("Analyze"):
    if uploaded_file and job_desc:
        resume_text = extract_text(uploaded_file)
        result, rank = analyze(resume_text, job_desc)

        st.write("Result:", result)
        st.write("Rank:", rank)

        # Communication message
        if rank == "High Rank":
            st.success("You are shortlisted for interview")
        else:
            st.error("You are not selected")

# Interview scheduling
st.subheader("Schedule Interview")
date = st.date_input("Select Date")
time = st.time_input("Select Time")

if st.button("Schedule"):
    st.success(f"Interview scheduled on {date} at {time}")