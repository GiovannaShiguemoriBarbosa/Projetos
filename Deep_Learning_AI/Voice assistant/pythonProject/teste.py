import pyttsx3

robo = pyttsx3.init()

# for voz in robo.getProperty('voices'):
#     print(voz)

# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0

robo.setProperty( name='voice', value= r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
robo.setProperty( name='volume', value=1.0)#volume máximo
robo.setProperty( name= 'rate', value=150)#palavras por min

robo.say("Olá Lucas, Tudo bem?")
robo.runAndWait()

robo.say("Vamos comprar pizza hoje?")
robo.runAndWait()