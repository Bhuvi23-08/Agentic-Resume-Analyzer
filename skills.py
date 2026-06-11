def skills_agent(llm, resume_text):
    prompt = f"""
Extract technical and soft skills from this resume.
Give bullet points only.

Resume:
{resume_text}
"""

    return llm.invoke(prompt).content