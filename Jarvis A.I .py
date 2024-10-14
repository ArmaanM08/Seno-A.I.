import speech_recognition as sr
import os

def say(text):
    os.system(f"say{text}")
    
say("Hello I am Jarvis A.I.")