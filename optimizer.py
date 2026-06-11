def optimizer_agent(llm, resume_text):
    prompt = f"""
Give resume improvement suggestions.

Resume:
{resume_text}
"""

    return llm.invoke(prompt).content