from flask import Flask
from agents import LeadAgent, PlanAgent

app = Flask(__name__)

@app.route('/')
def home():
    return "ZenDay: Your personal assistant to clear noise and prevent drift."

if __name__ == "__main__":
    app.run(debug=True)
