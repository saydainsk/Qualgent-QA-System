# verifier_agent.py
from utils.llm_utils import call_llm

class VerifierAgent:
    def __init__(self):
        pass

    def verify(self, subgoal: str, ui_tree: dict) -> bool:
        prompt = f"""
        Subgoal: "{subgoal}"
        Given the current UI hierarchy: {ui_tree}
        Has the subgoal been successfully completed? Reply only with 'Yes' or 'No'.
        """
        response = call_llm(prompt)
        return response.lower().startswith("yes")
