from datetime import datetime

def get_timestamp():
    """
    Returns current timestamp.
    """

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


def export_chat(messages):

    text=""

    for msg in messages:

        timestamp = msg.get("time", "No Timestamp")
        role = msg.get("role", "unknown").upper()
        content = msg.get("content", "")

        text += f"[{timestamp}]\n"
        text += f"{role}:\n"
        text += f"{content}\n\n"
        
        #text += f"[{msg['time']}]\n"
        #text += f"{msg['role'].upper()}:\n"
        #text += msg["content"]
        #text += "\n\n"

    return text
