# metrics_agent.py
def calculate_metrics(pre_task, post_task):
    # Time saved
    return post_task["time_spent"] - pre_task["time_spent"]
