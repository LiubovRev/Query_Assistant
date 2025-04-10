Query Assistant – Gemini Live Image Chat App
============================================

Overview
--------
Query Assistant is a desktop application built using Python and Gemini 1.5 Pro API
that allows users to interact with images in real-time. Users can upload an image
or capture it from a webcam, and ask questions about it via text or voice. The
responses are generated using Google's Gemini AI model and presented in a
chat-like interface.

Features
--------
- Upload or capture an image from webcam
- Start chat sessions with Gemini AI
- Ask questions via text or voice
- Get responses displayed in a chat window
- Hear AI responses using text-to-speech (TTS)
- Modern GUI with Tkinter

Requirements
------------
Install required dependencies:

    pip install fastapi
    pip install uvicorn
    pip install python-multipart
    pip install opencv-python
    pip install pygame
    pip install google.generativeai
    pip install SpeechRecognition
    pip install gtts
    pip install Pillow

You must also set your GEMINI API key either via environment variable
or by editing the placeholder in the code.

Usage
-----
1. Launch the application:
       python your_script_name.py

2. Use the interface to:
   - Upload an image or capture one with your camera.
   - Start a new session with Gemini.
   - Ask questions via typing or voice.
   - View and listen to AI responses.

API Key
-------
To run the app, you need a Gemini API key:
- Set it as an environment variable: `GEMINI_API_KEY=your_key`
- OR replace `"GEMINI_API_KEY"` in the script with your actual key (not recommended for production).

Components
----------
- `GeminiLiveApp` class: Main application logic and UI
- `setup_ui()`: Sets up the interface using Tkinter
- `start_session()`: Initializes a Gemini session with the image
- `send_message()`: Sends user query to the model
- `speak_text()`: Converts Gemini’s response to speech using gTTS
- `listen_for_speech()`: Captures audio input and converts it to text

Future Enhancements
-------------------
- Add image annotation or visual feedback
- Save chat history
- Support multiple languages
- Advanced safety configurations

