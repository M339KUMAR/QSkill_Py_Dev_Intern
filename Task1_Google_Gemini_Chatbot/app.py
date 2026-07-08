

print("Welcome to Gemini AI Chatbot")

import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
)

st.title("🤖 Gemini AI Chatbot")

user_input = st.text_area(
    "Ask me anything..."
)

if st.button("Generate Response"):

    if user_input.strip():

        with st.spinner("Thinking..."):

            answer = get_response(user_input)

        st.success("Response")

        st.write(answer)

    else:

        st.warning("Please enter a prompt.")
