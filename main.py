from re import search
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
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
        
        r.energy_threshold = 400

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(f"Error: {e}")  # Print actual error for debugging
        return "Some error occurred.. Sorry"

def storeCommand(query):
    l = []
    if query == True:
        l.append(query)
    else:
        pass


if __name__ == '__main__':
    print("Pycharm")
    say("Hello, I am SENO A.I.")
    
    sites = [
        ["google", "https://www.google.com"],
        ["youtube", "https://www.youtube.com"],
        ["facebook", "https://www.facebook.com"],
        ["wikipedia", "https://www.wikipedia.org"],
        ["amazon", "https://www.amazon.com"],
        ["twitter", "https://www.twitter.com"],
        ["my insta", "https://www.instagram.com/armaanmulani08/"],
        ["reddit", "https://www.reddit.com"],
        ["linked in", "https://www.linkedin.com/in/armaan-mulani-421bb9307/"],
        ["netflix", "https://www.netflix.com"],
        ["yahoo", "https://www.yahoo.com"],
        ["bing", "https://www.bing.com"],
        ["whatsapp", "https://www.whatsapp.com"],
        ["quora", "https://www.quora.com"],
        ["twitch", "https://www.twitch.tv"]]


    while True:
        query = takeCommand()
        if "some error" in query.lower():
            continue  # Skip iteration if an error occurred
        
        elif "search" in query.lower():
            query
            se = query.lower().split()
            se.remove("search")
            schr = ""
            for i in se:
                schr = schr + i + "+"
            webbrowser.open(f"https://www.google.com/search?q={schr}")
            
            
        elif "quit" in query.lower():
            break
        
            
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say("Yes Boss, opening " + site[0])
                webbrowser.open(site[1])
                #storeCommand(query)
                
