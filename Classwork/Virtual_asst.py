import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb

#Initialize the text-to-speech engine
engine=pyttsx3.init()

#Function to make the assistant speak
def speak(text):
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

#Function to listen to user's voice
def listen(): #voice as input and text as output
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold=1

        audio=recognizer.listen(source)
        try:
            command=recognizer.recognize_google(audio,language='en-in')
            print("🗣You said:",command)
            return command.lower()
        except:
            pass

