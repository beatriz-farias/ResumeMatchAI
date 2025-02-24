from .pdf_to_text import pdf_to_txt
from .preprocess import preprocess_text
from .similarity import compute_similarity

def job_resume_matcher(job_description_path, resume_path):
    job_description_text = pdf_to_txt(job_description_path)
    resume_text = pdf_to_txt(resume_path)
    
    job_description_clean = preprocess_text(job_description_text)
    resume_clean = preprocess_text(resume_text)
    print('job description')
    print(job_description_clean)
    print('resume')
    print(resume_clean)
    similarity_score = compute_similarity(job_description_clean, resume_clean)
    
    return similarity_score