# supervisor_agent.py
from utils.llm_utils import call_llm

class SupervisorAgent:
    def __init__(self):
        pass

    def analyze(self, logs: list[dict], trace_images: list[str] = None) -> str:
        summary_prompt = f"""
        Review this QA test trace and logs:

        {logs}

        1. Was the plan optimal and efficient?
        2. Were there any failures or unexpected UI states?
        3. Suggest ways to improve the prompt or Planner Agent strategy.
        4. Propose additional test cases to improve coverage.
        """
        return call_llm(summary_prompt)
