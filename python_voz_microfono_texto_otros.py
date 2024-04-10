#pip3 install SpeechRecognition
#pip install pyaudio
#pip install pyflac

import speech_recognition as sr
import pyaudio
import pyttsx3


voz = sr.Recognizer()
motor_voz = pyttsx3.init()

print("\nEscuchando...")

with sr.Microphone() as fuente:
    voz.adjust_for_ambient_noise(fuente)
    audio = voz.listen(fuente)

    try:
        texto = voz.recognize_google(audio,language='es-ES')
        print("\nTexto reconocido: " + texto)
    except sr.UnknownValueError:
        try:
            texto = voz.recognize_google(audio, language='en-US')
            print("\nTexto reconocido: " + texto)
        except sr.UnknownValueError:
            try:
                texto = voz.recognize_google(audio, language='ko-KR')
                print("\nTexto reconocido: " + texto)
            except sr.UnknownValueError:
                print("\nNo se pudo entender el audio en ningun idioma")
if 'texto' in locals():
    print("\nTexto reconocido: " + texto)
    motor_voz.say(texto)
    motor_voz.runAndWait()