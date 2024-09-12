import speech_recognition as sr

reconhecedor = sr.Recognizer()

caminho = r"C:\Users\lucas\Downloads\pythonProject\palmeiras.wav"

with sr.AudioFile(caminho) as arquivo:
    audio = reconhecedor.record(arquivo)
    texto = reconhecedor.recognize_google(audio, language="pt")
    print(texto)