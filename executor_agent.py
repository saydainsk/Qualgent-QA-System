# executor_agent.py
from android_env.environment import AndroidEnv
from utils.ui_parser import find_element_id_by_text

class ExecutorAgent:
    def __init__(self, task_name: str):
        self.env = AndroidEnv(task_name=task_name)
        self.ui_tree = self.env.reset()

    def execute(self, subgoal: str) -> dict:
        element_id = find_element_id_by_text(self.ui_tree, subgoal)
        if not element_id:
            return {"error": "Element not found", "subgoal": subgoal}

        action = {
            "action_type": "touch",
            "element_id": element_id
        }

        obs, reward, done, info = self.env.step(action)
        self.ui_tree = obs  # update internal state

        return {
            "action": action,
            "result_ui": obs,
            "reward": reward,
            "done": done,
            "info": info
        }
