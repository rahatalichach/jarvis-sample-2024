import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("good morning")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am AI. How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="enlish")
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Say that again, please...")
        return "none"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "none"

    return query.lower()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()

        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif "open google" in query:
            webbrowser.open("https://www.google.com")

        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif "open vs code" in query:
            code_path = "D:\\Users\\rahaat\\AppDataS\\Local\\Program\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "play song" in query:
            song_name = query.replace("play song", "").strip()
            speak(f"Playing song {song_name}")
            pywhatkit.playonyt(song_name)
