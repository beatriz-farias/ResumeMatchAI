from sentence_transformers import SentenceTransformer, util

def compute_similarity(job_description, resume):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embedding = model.encode(resume, convert_to_tensor=True)
    similarity_score = util.cos_sim(job_embedding, resume_embedding).item()
    return similarity_score