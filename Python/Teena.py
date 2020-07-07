from gtts import gTTS
from mutagen.mp3 import MP3
import os
import time
import datetime
import wikipedia
import webbrowser
import subprocess
import speech_recognition as sr

def speakout(text):
    myobj = gTTS(text=text, lang='en', slow=False)

    myobj.save("Testing.mp3")
    os.system("Testing.mp3")

    mp3 = int(MP3("Testing.mp3").info.length)
    print(mp3)
    time.sleep(mp3)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speakout("Good Morning!")

    elif hour>=12 and hour<18:
        speakout("Good Afternoon!")   

    else:
        speakout("Good Evening!")  

    speakout("I'm Teena. How can I help you...")

def listening():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
            
        print("say something...")
        audio = r.listen(source)                            
    try:
        voice = r.recognize_google(audio, language='en-in')  
        print(f"you said {voice}.")
    except:
        print("Can you say that again...")
        return 'None'
    return voice

if __name__ == "__main__":
    wishMe()
    
    while True:
        MyText = listening().lower()

        if MyText == 'how are you':
            result = "I'm fine. Thanks for asking. How are you?"
            speakout(result)

        elif 'good night' in MyText:
            print("Good night :)")
            result = "Good night. Sweet dreams."
            speakout(result)
            exit()

        elif 'wikipedia' in MyText:
            print("Searching...")
            MyText = MyText.replace("wikipedia", "")
            result = wikipedia.summary(MyText, sentences=1)
            speakout(result)

        elif 'play music' in MyText or 'open spotify' in MyText:
            subprocess.Popen("%s"%r'C:\Users\91957\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe')
