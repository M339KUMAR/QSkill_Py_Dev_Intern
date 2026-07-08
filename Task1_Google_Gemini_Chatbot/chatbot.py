from google import genai
from google.genai import types
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def get_response(history):
#def get_response(prompt: str) -> str:

    """
    Sends a prompt to Gemini and returns the response.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history,  #prompt
    )

    return response.text


#from google import genai
#from config import GEMINI_API_KEY

#client = genai.Client(api_key=GEMINI_API_KEY)


#def get_response(history):

#    response = client.models.generate_content(

#        model="gemini-2.5-flash",

#        contents=history,

#    )

#    return response.text

def create_chat():

    chat = client.chats.create(
        model="gemini-2.5-flash"
    )

    return chat


def send_message(chat, prompt):

    response = chat.send_message(
        prompt
    )

    return response.text
