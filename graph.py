from typing import TypedDict
from langgraph.graph import StateGraph, END

from utils.llm import load_llm

from agents.analyzer import analyzer_agent
from agents.skills import skills_agent
from agents.optimizer import optimizer_agent
from agents.ats_score import ats_agent
from agents.job_match import job_match_agent
from agents.interview import interview_agent
from agents.report import report_agent

llm = load_llm()


class ResumeState(TypedDict):
    resume_text: str
    job_description: str
    analysis: str
    skills: str
    suggestions: str
    ats: str
    job_match: str
    questions: str
    final_report: str


def analyze_node(state):
    state["analysis"] = analyzer_agent(llm, state["resume_text"])
    return state


def skills_node(state):
    state["skills"] = skills_agent(llm, state["resume_text"])
    return state


def optimizer_node(state):
    state["suggestions"] = optimizer_agent(llm, state["resume_text"])
    return state


def ats_node(state):
    state["ats"] = ats_agent(llm, state["resume_text"])
    return state


def job_match_node(state):
    if state["job_description"]:
        state["job_match"] = job_match_agent(
            llm,
            state["resume_text"],
            state["job_description"]
        )
    else:
        state["job_match"] = "No Job Description Provided"

    return state


def interview_node(state):
    state["questions"] = interview_agent(
        llm,
        state["resume_text"]
    )
    return state


def report_node(state):
    state["final_report"] = report_agent(
        state["analysis"],
        state["skills"],
        state["suggestions"],
        state["ats"],
        state["job_match"],
        state["questions"]
    )
    return state


def build_graph():

        graph = StateGraph(ResumeState)  # type: ignore


        graph.add_node("analyzer", analyze_node)
        graph.add_node("skills", skills_node)
        graph.add_node("optimizer", optimizer_node)
        graph.add_node("ats", ats_node)
        graph.add_node("job_match", job_match_node)
        graph.add_node("interview", interview_node)
        graph.add_node("report", report_node)

        graph.set_entry_point("analyzer")

        graph.add_edge("analyzer", "skills")
        graph.add_edge("skills", "optimizer")
        graph.add_edge("optimizer", "ats")
        graph.add_edge("ats", "job_match")
        graph.add_edge("job_match", "interview")
        graph.add_edge("interview", "report")
        graph.add_edge("report", END)

        return graph.compile()