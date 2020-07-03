import os
import time
import pyttsx3
import wikipedia
from gtts import gTTS
from mutagen.mp3 import MP3
import speech_recognition as sr

r = sr.Recognizer()

language = 'en'

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("say something...")
            audio = r.listen(source)
            MyText = r.recognize_google(audio)
            print(MyText)
            result = wikipedia.summary(MyText, sentences=1)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    
    except:
        result = "Unknown error occured while listening or searching..."

    finally:
        myobj = gTTS(text=result, lang=language, slow=False)
        myobj.save("Testing.mp3")
        os.system("Testing.mp3")
        audio = int(MP3("Testing.mp3").info.length)
        print(audio)
        time.sleep(int(MP3("Testing.mp3").info.length)+2)
