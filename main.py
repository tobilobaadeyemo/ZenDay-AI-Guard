# main.py
from agents import lead_agent, plan_agent

def main():
    user_input = "schedule my task"
    action = lead_agent.lead_agent(user_input)
    print(action)

if __name__ == "__main__":
    main()
