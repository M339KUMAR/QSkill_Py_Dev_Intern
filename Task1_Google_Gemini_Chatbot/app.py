

print("Welcome to Gemini AI Chatbot")

import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
)

st.title("🤖 Gemini AI Chatbot")

#user_input = st.text_area(
#    "Ask me anything..."
#)

#if st.button("Generate Response"):

#    if user_input.strip():

#        with st.spinner("Thinking..."):

#            answer = get_response(user_input)

#        st.success("Response")

#        st.write(answer)

#    else:

#        st.warning("Please enter a prompt.")
#import streamlit as st
#from chatbot import get_response

#st.set_page_config(
#    page_title="Gemini AI Chatbot",
#    page_icon="🤖",
#)

#st.title("🤖 Gemini AI Chatbot")

# -----------------------------
# Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Display user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Gemini response
    with st.spinner("Thinking..."):

        response = get_response(prompt)

    st.chat_message("assistant").markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
