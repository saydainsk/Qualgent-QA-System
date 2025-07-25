from planner_agent import PlannerAgent
from executor_agent import ExecutorAgent
from verifier_agent import VerifierAgent
from supervisor_agent import SupervisorAgent

class AgentController:
    def __init__(self, task_name, goal):
        self.goal = goal
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent(task_name)
        self.verifier = VerifierAgent()
        self.supervisor = SupervisorAgent()
        self.logs = []

    def run(self):
        plan = self.planner.plan(self.goal)
        for subgoal in plan:
            result = self.executor.execute(subgoal)
            passed = self.verifier.verify(subgoal, result.get("result_ui", {}))

            self.logs.append({
                "subgoal": subgoal,
                "action": result.get("action", {}),
                "verdict": "pass" if passed else "fail"
            })

            if not passed:
                plan = self.planner.plan(f"Replan due to failure on: {subgoal}")
                return self.run()  # recursive retry

        feedback = self.supervisor.analyze(self.logs)
        self.logs.append({"supervisor_feedback": feedback})
        return self.logs
