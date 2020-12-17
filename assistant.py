import speech_recognition as sr
import time
import webbrowser
import playsound
from gtts import gTTS
import random
import os

r = sr.Recognizer()

def speech(audio_string):
    texttospeech = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 2000000)
    audio_file = 'au-' + str(r) +'.mp3'
    texttospeech.save(audio_file)

    playsound.playsound(audio_file)

    print(audio_string)
    os.remove(audio_file)

def take_audio(reply = False):
    with sr.Microphone() as source:
        if reply:
            speech(reply)
        
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speech("Sorry! Enakku puriyala")
        except sr.RequestError:
            speech("Sorry! Ippa work panna mudiyaadhu")

        return voice_data

def response(voice_data):
    if 'what is your name' in voice_data:
        speech("My name Assistant")
    
    if "time" in voice_data:
        speech(time.ctime())
    
    if 'search' in voice_data:
        search = take_audio('Enna search pannanum?')
        url = f'https://google.com/search?q={search}'

        webbrowser.open(url)

        speech(f"unga {search} kaana result ready!")
    
    if 'stop' in voice_data:
        speech("ok Bye!")
        exit()

speech("Enna pannanum sollunga!")
time.sleep(1)

while 1:
    voice_data = take_audio()

    response(voice_data)