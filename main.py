import speech_recognition as sr
import os
import webbrowser



def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error Occured.. Sorry"


if __name__ == '__main__':
    print("Pycharm")
    say("Hello I am Jarvis A.I.")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["aniwatch","https://www.aniwatchtv.to"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say("Yes Boss")
                webbrowser.open(site[1])
