import speech_recognition as sr
import pyttsx3
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            print(e)
            return ""
    return query.lower()

def time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def main():
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        query = listen()
        if "time" in query:
            time()
        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
