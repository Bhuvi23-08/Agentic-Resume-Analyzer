def job_match_agent(llm, resume_text, job_description):
    prompt = f"""
Compare resume with job description.

Give:
1. Match percentage
2. Matching skills
3. Missing skills
4. Recommendation

Resume:
{resume_text}

Job Description:
{job_description}
"""

    return llm.invoke(prompt).content