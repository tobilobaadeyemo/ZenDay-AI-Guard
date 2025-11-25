# ZenDay-AI-Guard
ZenDay is an autonomous assistant designed to clear noise and prevent task drift, ensuring users stay focused and productive. ZenDay is built with a multi-agent system using Google’s GenAI SDK.

## Features:
- Multi-agent orchestration.
- Contextual task management.
- Optimized schedule handling.

## Getting Started:
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run: `python main.py`.

## Agents:
- `lead_agent.py`: Handles user input.
- `plan_agent.py`: Plans tasks based on user priorities.
- `metrics_agent.py`: Calculates time saved.
- `keep_agent.py`: Manages user preferences.
- `tidy_agent.py`: Adjusts the schedule.
- `mail_agent.py`: Handles email tasks.
- `meet_agent.py`: Manages meetings.
- `memory_agent.py`: Stores memory of user preferences.
