# planner_agent.py
from utils.llm_utils import call_llm  # A helper that wraps OpenAI or Gemini API

class PlannerAgent:
    def __init__(self):
        pass

    def plan(self, goal: str) -> list[str]:
        prompt = f"""
        Given the high-level QA task: "{goal}", break it down into a sequence of UI subgoals for an Android app. 
        Each step should be specific, grounded, and independent.
        """
        response = call_llm(prompt)
        return [line.strip("-• ") for line in response.strip().split("\n") if line.strip()]
