from agent_controller import AgentController
import json

if __name__ == "__main__":
    goal = "Test turning Wi-Fi on and off"
    controller = AgentController(task_name="settings_wifi", goal=goal)
    logs = controller.run()

    with open("qa_logs.json", "w") as f:
        json.dump(logs, f, indent=2)

    print("QA Test Run Complete ✅ — Logs saved to qa_logs.json")
