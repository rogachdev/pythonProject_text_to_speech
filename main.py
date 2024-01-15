from gtts import gTTS
import os

# abre o arquivo txt na raiz do proejto.
file = open("text.txt", "r").read()

# converte o arquivo txt na linguagem pt-br
speech = gTTS(text=file, lang='pt-br', slow=False)

# cria uma versáo .mp3 do arquivo txt e salva na raiz do projeto
speech.save("textVoice.mp3")

#abre o arquivo criado na estensão .mp3
os.system("textVoice.mp3")
