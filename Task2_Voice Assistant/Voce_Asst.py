"""
Streamlit Voice Assistant
--------------------------
Click the mic button ONCE to start recording, click it AGAIN to stop.
The recorded audio is then converted to text automatically.

Note: Streamlit apps run in the browser and re-run the script on every
interaction, so a true "press-and-hold" button (like a native desktop app)
isn't supported. Click-to-start / click-to-stop is the standard and most
reliable pattern for voice recording in Streamlit.

Requirements (install first):
    pip install streamlit
    pip install streamlit-mic-recorder
    pip install SpeechRecognition

Run with:
    streamlit run voice_assistant_streamlit.py
"""

import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import io

st.set_page_config(page_title="Voice Assistant", page_icon="🎤", layout="centered")

st.title("🎤 Voice Assistant")
st.caption("Click the mic to start recording, click again to stop.")

recognizer = sr.Recognizer()

# mic_recorder renders a button with a mic icon.
# It returns a dict with 'bytes' (the recorded audio, WAV format) once
# recording stops, or None while idle / before first use.
audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹️ Stop Recording",
    just_once=False,      # keep the widget available for repeated recordings
    use_container_width=True,
    format="wav",
    key="recorder",
)

if audio is not None and audio.get("bytes"):
    st.audio(audio["bytes"], format="audio/wav")

    with st.spinner("Transcribing..."):
        try:
            audio_file = io.BytesIO(audio["bytes"])
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)

            text = recognizer.recognize_google(audio_data)
            st.success("Transcription:")
            st.write(text)

            # Keep a running transcript across recordings in this session
            if "transcript_history" not in st.session_state:
                st.session_state.transcript_history = []
            st.session_state.transcript_history.append(text)

        except sr.UnknownValueError:
            st.error("Could not understand the audio. Please try again.")
        except sr.RequestError as e:
            st.error(f"Speech recognition API error: {e}")

# Show history of everything transcribed this session
if st.session_state.get("transcript_history"):
    st.divider()
    st.subheader("Session Transcript History")
    for i, line in enumerate(st.session_state.transcript_history, 1):
        st.write(f"{i}. {line}")
