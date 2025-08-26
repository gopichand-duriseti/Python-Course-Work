import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='en-in')
            print("🗣 You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("❌ Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""

# Function to respond to voice commands
def run_assistant():
    speak("Hello! I'm your assistant. How can I help you?")
    while True:
        command = listen()
        if 'time' in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f'The present time is {now}')
        elif 'date of birth' in command:
            speak('Your Date of Birth is 23rd February 2001')
        elif 'your name' in command:
            speak("I'm your python assistant")
        elif 'date' in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif 'open google' in command:
            speak("Opening Google")
            wb.open("https://www.google.com")
        elif 'stop' in command or 'exit' in command or 'bye' in command:
            speak("okay bye bye! have a good day")
            break
        else:
            speak("Sorry, I can't do that yet.")

run_assistant()
