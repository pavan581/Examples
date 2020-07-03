import os
import time
import wikipedia
from gtts import gTTS
from mutagen.mp3 import MP3
import speech_recognition as sr

#initilisation of recognizer
r = sr.Recognizer()

#default language for wikipedia search
language = 'en'

#Runs untill stopped
while True:
    
    try:
        
        with sr.Microphone() as source:

            #adjust for surrounding noise
            r.adjust_for_ambient_noise(source)
            
            print("say something...")
            audio = r.listen(source)                        #listen for input
            MyText = r.recognize_google(audio)              #convert input to string
            print(MyText)
            result = wikipedia.summary(MyText, sentences=1) #search for the input in wikipedia 

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except:
        result = "Unknown error occured while listening or searching..."

    finally:

        #gTTS google Translate To Speech
        myobj = gTTS(text=result, lang=language, slow=False)

        myobj.save("Testing.mp3")
        os.system("Testing.mp3")

        audio = int(MP3("Testing.mp3").info.length)
        print(audio)
        time.sleep(audio)
