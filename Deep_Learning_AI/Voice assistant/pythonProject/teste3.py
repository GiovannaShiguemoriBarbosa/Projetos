import pyttsx3

robo = pyttsx3.init()
robo.setProperty(name='volume', value=200.0)
robo.setProperty(name='voice', value=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
robo.setProperty(name='rate', value=160)

with open('livro.txt', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)
    robo.say(texto)
    robo.runAndWait()

