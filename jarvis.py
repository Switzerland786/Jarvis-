import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import os
import json
import requests

engine = pyttsx3.init('sapi5')
engine.setProperty('rate',150)

engine.setProperty('volume',1)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hi sir I am Your Jarvis May I help you")


def takeCommand():
       r = sr.Recognizer()
       with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 1
         audio = r.listen(source)
       try:
          print("Recognition....")
          query = r.recognize_google(audio,language="en-in")
          print(f"User said: {query}\n")
       except Exception as e:
           print("Say that please again")
           return "None"
       return query

if __name__ == '__main__':
     wishme()
     while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak("Searching wikipedia")
           query = query.replace("wikipedia", "")
           result = wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(result)
           speak(result)
       elif 'open youtube' in query:
           webbrowser.open("Youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'open facebook' in query:
           webbrowser.open("facebook.com")
       elif 'open learn me fast' in query:
           webbrowser.open("learnmefast.com")
       elif 'play music' in  query:
           music = 'D:\\songg'
           songs = os.listdir(music)
           print(songs)
           os.startfile(os.path.join(music,songs[0]))
       elif 'news' in query:
           news = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=8b01459a0137490fa1edf2d8714ea695")
           news = json.loads(news.text)
           arts = news['articles']
           speak("Today Top 10 news begin now listen carefully")
           for art in arts:
            speak(art['description'])
       #elif 'play video' in query:
        #   vid = 'D:\\video'
        #   videos = os.listdir(vid)
         #  print(videos)
         #  os.startfile(os.path.join(vid, videos[0]))
       elif 'live score' in query:
           score = requests.get("http://cricapi.com/api/cricketScore?unique_id=918033&apikey=ll9fUfC8cXg3NJSc613U4EXqffl1")
           score = json.loads(score.text)
           live = score['stat']
           speak("Today cricket score")
           speak(live)





