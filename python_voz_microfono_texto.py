import speech_recognition as sr
from pocketsphinx import LiveSpeech
import pyaudio

# python_voz_microfono_texto.py
#
# pip3 install SpeechRecognition
#
# apt install python3-pyaudio
# apt install flac


voz = sr.Recognizer()

print("\nEscuchando...")

with sr.Microphone() as fuente:
    voz.adjust_for_ambient_noise(fuente)
    audio = voz.listen(fuente)
    texto = voz.recognize_sphinx(audio)

print("\nTexto: ", texto)
