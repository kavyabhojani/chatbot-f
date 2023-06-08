import pyttsx3
import speech_recognition as sr
import openai
from tkinter import *
import threading

# Set up OpenAI API credentials
openai.api_key = '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'

# Set up speech recognition
recognizer = sr.Recognizer()

# Set up text-to-speech
engine = pyttsx3.init()

# Set up voice recognition
def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Sorry, an error occurred.")
        return ""

# Set up text-to-speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Chat with GPT
def chat_with_gpt(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        echo=True
    )
    return response.choices[0].text.strip()

# Voice recognition thread
def voice_recognition_thread():
    while True:
        user_input = speech_to_text()

        if user_input:
            response = chat_with_gpt(user_input)
            print("Chatbot: ", response)
            text_to_speech(response)

# Callback for microphone button
def microphone_button_callback():
    threading.Thread(target=voice_recognition_thread).start()

# GUI setup
root = Tk()

mic_button = Button(root, text="Press to record", command=microphone_button_callback)
mic_button.pack()

root.mainloop()
