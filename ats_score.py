def ats_agent(llm, resume_text):
    prompt = f"""
Act as an ATS checker.

Give:
1. ATS Score out of 100
2. Missing keywords
3. Improvement tips

Resume:
{resume_text}
"""

    return llm.invoke(prompt).content