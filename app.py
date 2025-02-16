import streamlit as st
from src.smart_matcher import smart_matcher

st.title("Resume Match AI")

job_description_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")
resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if job_description_file and resume_file:
    with open("temp_job_description.pdf", "wb") as f:
        f.write(job_description_file.getbuffer())
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.getbuffer())
    
    score = smart_matcher("temp_job_description.pdf", "temp_resume.pdf")
    st.write(f"Compatibility Score: {score:.2f}")