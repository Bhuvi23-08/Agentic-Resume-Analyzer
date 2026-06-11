def analyzer_agent(llm, resume_text):
    prompt = f"""
Analyze this resume and give a short candidate summary.

Resume:
{resume_text}
"""

    return llm.invoke(prompt).content