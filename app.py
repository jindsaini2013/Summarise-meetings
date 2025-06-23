import os
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"


import streamlit as st
import whisper
import ollama
import os

# Load Whisper model once
model = whisper.load_model("base")

# Title
st.title("Meeting Transcript and Summary")

# File uploader
audio_file = st.file_uploader("Upload your audio file (.mp3/.wav)", type=["mp3", "wav"])

if audio_file:
    with st.spinner("Transcribing..."):
        # Save uploaded file to disk
        upload_path = os.path.join("uploads", audio_file.name)
        os.makedirs("uploads", exist_ok=True)
        with open(upload_path, "wb") as f:
            f.write(audio_file.read())

        # Transcribe
        result = model.transcribe(upload_path)
        transcript = result["text"]
        st.subheader("Transcript")
        st.write(transcript)

        # Summarize
        with st.spinner("Summarizing..."):
            messages = [{"role": "user", "content": "Summarize this:\n" + transcript}]
            response = ollama.chat(model="llama3.2", messages=messages)
            summary = response["message"]["content"]

        st.subheader("Summary")
        st.write(summary)
