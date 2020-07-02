import wikipedia
import os
from gtts import gTTS

search_word = input("Wikipedia> ")
language = 'en'

myobj = gTTS(text=wikipedia.summary(search_word, sentences=1))
myobj.save("Testing.mp3")
os.system("Testing.mp3")

