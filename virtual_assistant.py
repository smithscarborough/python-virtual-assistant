import speech_recognition as sr
import os
import time
import pyowm
import random
import smtplib
import pyjokes
import playsound
import pywhatkit
import wikipedia
import webbrowser
from gtts import gTTS
from time import ctime
from dotenv import load_dotenv
load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone(device_index=0) as source:
        if ask:
            cinnamon_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            cinnamon_speak('Sorry, I didn\'t get that.')
        except sr.RequestError:
            cinnamon_speak('I do apologize; I seem to be having trouble hearing you right now.')
        return voice_data

def cinnamon_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en-au')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what\'s your name' in voice_data:
        cinnamon_speak('My name is Cinnamon.')
    if 'pretty' in voice_data:
        cinnamon_speak('Thank you so much.  You are too sweet. What is your name?')
    if 'Smith' in voice_data:
        cinnamon_speak('Now THAT is a great name!  It is so nice to meet you Smith.')
    if 'how are you' in voice_data:
        cinnamon_speak('I\'m doing well Smith! Thank you for asking.')
    if 'where are you from' in voice_data:
        cinnamon_speak('I am actually a spawn of satan from the depths of hell.')
    if 'are you hot' in voice_data:
        cinnamon_speak('I\'m code.')
    if 'what time is it' in voice_data:
        cinnamon_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What would you like to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        cinnamon_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        cinnamon_speak('Here is the location of ' + location)
    if 'who is' in voice_data:
        person = voice_data.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        cinnamon_speak(info)
    if 'get info on' in voice_data:
        thing = voice_data.replace('get info on', '')
        info = wikipedia.summary(thing, 1)
        print(info) 
        cinnamon_speak(info)
    if 'joke' in voice_data:
        cinnamon_speak(pyjokes.get_joke())
    if 'funny' in voice_data:
        cinnamon_speak('You\'re too kind. I\'m here every night.')
    if 'play' in voice_data:
        song = voice_data.replace('play', '')
        cinnamon_speak('playing ' + song)
        pywhatkit.playonyt(song)
    if 'Spotify' in voice_data:
        url = 'https://open.spotify.com/playlist/111l1ee4pbWApbbZ2JGAgp:play'
        print(url)
        webbrowser.get().open(url)
    if 'horoscope' in voice_data: 
        sign = record_audio('What is your sign?')
        which_sign = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
        print(sign)
        if sign in which_sign:
            cinnamon_speak('Here\'s what I found for ' + sign)
            url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=' + str(which_sign.index(sign) + 1)
            webbrowser.get().open(url)
    if 'send email' in voice_data:
        def send_email(recipient = record_audio('Who would you like to email?')):
            email_contacts = {
                'me': 'smithscarborough@gmail.com',
                'myself': 'smithscarborough@gmail.com',
                'cole': 'stantoncbradley@gmail.com',
                'chitananda': 'chitananda@sfawakenedmind.org',
                'sandy': 'sandy708@sbcglobal.net',
                'stuart': 'stuartms@sbcglobal.net',
                'court': 'courtneymunson@gmail.com',
                'tracey': 'tchavez@azurehoustonapts.com',
                'caleb rogers': 'caleb@calebjay.com',
                'judy': 'jnjjuju@aol.com',
                'cat vet clinic': 'info@catvetclinic.com',
                'katherine': 'katherine@digitalcrafts.com'
            }
            try:
                email_recipient = email_contacts[recipient]
                email_message = record_audio('What would you like to say?')
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(USER, PASSWORD)
                server.sendmail('smithscarborough@gmail.com', email_recipient, email_message + '.' + '\n\n-Sent from Cinnamon, Virtual Assistant') 
                webbrowser.get().open('https://mail.google.com/mail/u/0/#inbox')
                cinnamon_speak('Alright! Message sent.')
            except:
                cinnamon_speak('I\'m having trouble finding that name Smith.')
        send_email()
    if 'that\'s all' in voice_data:
        cinnamon_speak('Okay Smith, I\'m right here if you need anything else.')
        exit()
    if 'that\'s it' in voice_data:
        cinnamon_speak('Okay Smith, I\'m right here if you need anything else.')
        exit()
    if 'nevermind' in voice_data:
        cinnamon_speak('Okay Smith, I\'m right here if you need anything else.')
        exit()
    if 'goodnight' in voice_data:
        cinnamon_speak('Goodnight Smith.')
        exit()

time.sleep(2)
cinnamon_speak('Hello! How may I help you?')

while True:
    voice_data = record_audio()
    respond(voice_data)