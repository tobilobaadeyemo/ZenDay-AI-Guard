class PlanAgent:
    def __init__(self):
        self.name = "Plan Agent"
    
    def schedule_task(self, task):
        # Logic for scheduling
        return f"Task {task} scheduled."

def main():
    agent = PlanAgent()
    print(agent.schedule_task("Meeting with the team"))

if __name__ == "__main__":
    main()
