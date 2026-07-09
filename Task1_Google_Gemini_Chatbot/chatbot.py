from google import genai
from google.genai import types
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

personality ='Teacher'

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
    """
    Now Gemini can automatically use Google Search 
    when it determines that current information 
    is needed.
    """
    response = chat.send_message(
        prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                          )
                  ]
         )
     )
    return response.text


SYSTEM_PROMPTS = {

    "General Assistant":
        "You are a helpful AI assistant.",

    "Python Expert":
        "You are an experienced Python developer.",

    "Data Scientist":
        "You are an expert in Data Science and Machine Learning.",

    "Career Coach":
        "You help candidates prepare for interviews.",

    "Teacher":
        "Explain concepts step-by-step using simple language."
}

full_prompt = (
    SYSTEM_PROMPTS[personality]
    + "\n\n"
    + prompt
)
