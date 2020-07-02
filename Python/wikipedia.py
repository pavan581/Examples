import wikipedia
import os
from gtts import gTTS

language = 'en'

while True:
    search_word = input("Wikipedia> ")


    try:
        text = wikipedia.summary(search_word, sentences=1)
    except:
        text = "An unexpected error occured while searching."

    finally:
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("Testing.mp3")
        os.system("Testing.mp3")
        
