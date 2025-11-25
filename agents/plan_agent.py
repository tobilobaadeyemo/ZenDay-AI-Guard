# plan_agent.py
def plan_task(task_details):
    if task_details['importance'] > 5:
        return "Schedule as high priority"
    return "Low priority task"
