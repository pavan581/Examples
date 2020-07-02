import wikipedia
import os
from gtts import gTTS

search_word = input("Wikipedia> ")
language = 'en'
try:
    text = wikipedia.summary(search_word, sentences=1)
except:
    text = "An unexpected error occured while searching."

finally:
    myobj = gTTS(text=text)
    myobj.save("Testing.mp3")
    os.system("Testing.mp3")
