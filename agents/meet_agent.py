# meet_agent.py
def handle_meeting_conflict(existing_meeting, new_meeting):
    if new_meeting["time"] == existing_meeting["time"]:
        return "Conflict detected. Moving meeting"
    return "Meeting scheduled"
