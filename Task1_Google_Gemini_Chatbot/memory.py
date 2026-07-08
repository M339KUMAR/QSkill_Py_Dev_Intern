

def build_history(messages):
    """
    Convert Streamlit chat history into the format expected
    by the Gemini API.
    """

    history = []

    for message in messages:

        history.append(
            {
                "role": message["role"],
                "parts": [
                    {
                        "text": message["content"]
                    }
                ]
            }
        )

    return history
