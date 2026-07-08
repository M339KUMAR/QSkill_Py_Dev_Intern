from google import genai
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
