from gtts import gTTS
import os

file = open("text.txt", "r").read()

speech = gTTS(text=file, lang='pt-br', slow=False)
speech.save("textVoice.mp3")
os.system("textVoice.mp3")
