from datetime import datetime

def get_timestamp():
    """
    Returns current timestamp.
    """

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
