def interview_agent(llm, resume_text):
    prompt = f"""
Generate 5 interview questions based on this resume.

Resume:
{resume_text}
"""

    return llm.invoke(prompt).content