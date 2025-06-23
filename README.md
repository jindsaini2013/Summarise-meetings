# Summarise-meetings – Transcription + Summarization with LLMs

Automatically transcribe and summarize your `.mp3` or `.wav` meeting recordings using open-source AI — **Whisper** + **LLaMA3** (via Ollama), wrapped in a simple **Streamlit app**.

---

## 📌 Features

✅ Upload `.mp3` or `.wav` audio files  
✅ Transcription using `Whisper` (OpenAI speech-to-text model)  
✅ Summarization using `llama3.2` (via Ollama, runs locally)  
✅ Intuitive UI with Streamlit  
✅ 100% local – no API calls or data sharing

---

## 📌 Demo


<img width="1439" alt="Image" src="https://github.com/user-attachments/assets/48e9eeca-e41f-426e-bff3-2a47a961dfff" />

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/18682d9d-7c09-4b9e-9bc3-44e4979be405" />

---

## 📌 Tech Stack

- [Whisper](https://github.com/openai/whisper) for speech-to-text
- [Ollama](https://ollama.com) for running `llama3.2` locally
- [Streamlit](https://streamlit.io) for the web app
- Python + FFmpeg (for audio preprocessing)

---

## 📌 Setup Instructions
You can run this project locally using **Anaconda** in terminal.

---

### 1. Clone the repo:

git clone https://github.com/jindsaini2013/Summarise-meetings.git

cd meeting-minute-generator 

### 2. Create and activate environment:

conda env create -f environment.yml

conda activate llms

### 3. Run the app:

streamlit run app.py

### 4. Additional Setup
Make sure FFmpeg is installed and accessible from your system PATH.
