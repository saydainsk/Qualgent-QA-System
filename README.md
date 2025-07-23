# 🤖 Qualgent-QA-System

A multi-agent LLM-powered mobile QA automation system built on top of [Agent-S](https://github.com/simular-ai/Agent-S) and [android_world](https://github.com/google-research/android_world). Designed for testing Android UI workflows using reasoning, planning, execution, and verification agents.

---

'''
## 📁 Project Structure

Qualgent-QA-System/
├── agent_s/ # Forked Agent-S repository
├── planner_agent.py # LLM-based Planner
├── executor_agent.py # Executes subgoals via AndroidEnv
├── verifier_agent.py # Verifies whether a UI state matches expectations
├── supervisor_agent.py # Reviews trace + logs to suggest improvements
├── agent_controller.py # Orchestrates Planner → Executor → Verifier → Supervisor
├── test_run.py # Main script to run QA tests
├── qa_logs.json # Stores execution trace logs
├── requirements.txt # Python dependencies
├── setup.sh # Project setup script
└── README.md # This file

