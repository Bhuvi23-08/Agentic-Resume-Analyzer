def report_agent(
    analysis,
    skills,
    suggestions,
    ats,
    job_match,
    questions
):

    return f"""
AI RESUME ANALYSIS REPORT

1. Resume Analysis
{analysis}

2. Skills
{skills}

3. Suggestions
{suggestions}

4. ATS Score
{ats}

5. Job Match
{job_match}

6. Interview Questions
{questions}
"""