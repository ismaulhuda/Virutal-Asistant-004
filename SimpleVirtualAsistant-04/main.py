#importing necessary libraries.
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

#setting some variables
MASTER = "wesiyowesi"
firefox_path = 'Your firefox.exe path'
songs_dir = 'Your songs directory'
songs = 'Your songs'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#speak function will make a.i speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#this function will make hexa say "good morning" etc.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >=0 and hour <12:
        speak("Good Morning" + MASTER + "...")

    elif hour >=12 and hour <18:
        speak("Good Afternoon" + MASTER + "...")
    
    else:
        speak("Good Evening" + MASTER + "...")

    speak("Can I help you?...")

#this function will make jarvis to take commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please.")
        query = None
    
    return query


#Hexa starts from here:
speak("Hello my name is Hexa...")
wishMe()
query = takeCommand()


#first task is to search something from wikipedia.
if 'wikipedia' in query.lower():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "real madrid")
    results = wikipedia.summary(query, sentences = 2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

#perintah untuk membuka google, youtube, media sosial dan aplikasi.
elif 'open youtube' in query.lower():
    urL='https://www.youtube.com'
    firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
    webbrowser.get('firefox').open_new_tab(urL)
    
elif 'open google' in query.lower():
    urL='https://www.google.com'
    firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
    webbrowser.get('firefox').open_new_tab(urL)

elif 'open instagram' in query.lower():
    urL='https://www.instagram.com'
    firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
    webbrowser.get('firefox').open_new_tab(urL)
    
elif 'open facebook' in query.lower():
    urL='https://www.facebook.com'
    firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
    webbrowser.get('firefox').open_new_tab(urL)
    
elif 'open google scholar' in query.lower():
    urL='https://google.scholar.com'
    firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
    webbrowser.get('firefox').open_new_tab(urL)
    
elif 'play music' in query.lower():
    songs_dir="C:\\Users\\WIN10x64\\Music"
    songs=os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
    
#perintah untuk bertanya tentang waktu "what time it is?"    
elif 'time' in query.lower():
    strTime=datetime.datetime.now().strftime("%H:%M")
    speak(f"the time is {strTime}")
