from gtts import gTTS
from datetime import datetime
from pygame import mixer
from time import sleep
import os


meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}


agora = datetime.now()
# print(agora)
hora = agora.hour
minuto = agora.minute
print(hora)

dia = agora.today().day
mes = agora.today().month
ano = agora.today().year

msg = "Agora são" + str(hora) + "horas e" + str(minuto) + "minutos"
msg += "do dia" + str(dia) + "de" + meses[mes] + "de" + str(ano) 

voz = gTTS(msg, lang='pt-br')
voz.save("data.mp3")
mixer.init()
mixer.music.load("data.mp3")
mixer.music.play()
while mixer.music.get_busy():
    sleep(0.1)

os.system("palmeiras.mp3")

