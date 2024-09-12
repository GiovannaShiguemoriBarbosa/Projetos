from gtts import gTTS
from pygame import mixer
from time import sleep

voz = gTTS(text="Palmeiras não tem mundial", lang='pt-br')
voz.save('palmeiras.mp3')

mixer.init()
mixer.music.load('palmeiras.mp3')
mixer.music.play()
input("Digite ENTER para finalizar")

while mixer.music.get_busy():
    sleep(0.1)
