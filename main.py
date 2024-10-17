import speech_recognition as sr
import os
import webbrowser
import pyttsx3  # For cross-platform text-to-speech


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(f"Error: {e}")  # Print actual error for debugging
        return "Some error occurred.. Sorry"

def storeCommand():
    l = []
    if query == True:
        l.append(query)
    else:
        pass


if __name__ == '__main__':
    print("Pycharm")
    say("Hello, I am SENO A.I.")
    
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], 
             ["google", "https://www.google.com"], ["aniwatch", "https://www.aniwatchtv.to"]]

    while True:
        query = takeCommand()
        if "some error" in query.lower():
            continue  # Skip iteration if an error occurred

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say("Yes Boss, opening " + site[0])
                webbrowser.open(site[1])
