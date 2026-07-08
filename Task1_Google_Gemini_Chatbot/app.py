 

print("Welcome to Gemini AI Chatbot")
 
import streamlit as st
from chatbot import get_response
from chatbot import create_chat, send_message
from memory import build_history
from utils import export_chart, get_timestamp
from settings import AVAILABLE_MODELS

#--------------------------------------       
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
)

#st.title("🤖 Gemini AI Chatbot")
st.title("🤖 Gemini AI Assistant")

st.caption(
"Powered by Google Gemini • Memory • Google Search"
)

st.divider()
#--------------------------------------       
if "chat" not in st.session_state:

    st.session_state.chat = create_chat()
#---------------------------------------

with st.sidebar:

    st.header("Gemini AI Chatbot")

    st.markdown("-------")
 
    #st.write("### Features")
    st.subheader("Features")
    #st.write("✅ Chat Interface")
    st.success("Chat Interface")
    #st.write("⏳ Conversation Memory")
    st.success("Conversation Memory")
    #st.write("⏳ Google Search")
    st.success("Google  Search")
    selected_model = st.selectbox(
                                "Gemini Model",
                                AVAILABLE_MODELS
                                )
 
    st.write("⏳ Export Chat")
    chat_text=export_chat(
             st.session_state.messages
            )
 
    st.write("⏳ Chat History Download")
    st.download_button(
                     "📥 Download Chat",
                     chat_text,
                     file_name="chat_history.txt"
                     )
 
    st.info("Professional UI:")

    st.metric(
             "Messages",
             len(st.session_state.messages)
    )
    st.info(
    "Model: Gemini 2.5 Flash"
    )
 
    st.markdown("------------")

    if st.button("🆕 New Chat"):
    #if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat = create_chat()
        st.rerun()
#--------------------------------------       
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

        #response = get_response(prompt)
        history = build_history(st.session_state.messages)
        #response = get_response(history)
        try:
         #This prevents the app from crashing 
         #if there's an API or network issue.
         
            response = send_message(
                             st.session_state.chat,
                             prompt
                    )
        except Exception as e:
            response = f"Error: {e}"          

    st.chat_message("assistant").markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
