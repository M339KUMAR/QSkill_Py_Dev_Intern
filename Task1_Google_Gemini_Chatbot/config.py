import os
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
#GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )
