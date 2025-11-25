# lead_agent.py
def lead_agent(user_input):
    # Processes user input and routes to the correct agent
    if "move" in user_input:
        return "Moving the task"
    elif "schedule" in user_input:
        return "Scheduling a meeting"
