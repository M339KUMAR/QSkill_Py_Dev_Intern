from datetime import datetime

def get_timestamp():
    """
    Returns current timestamp.
    """

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


def export_chat(messages):

    text=""

    for msg in messages:

        text += f"[{msg['time']}]\n"

        text += f"{msg['role'].upper()}:\n"

        text += msg["content"]

        text += "\n\n"

    return text
