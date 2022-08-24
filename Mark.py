import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb
import os
import requests
from win10toast import ToastNotifier
import json

Mark = pyttsx3.init()
voice = Mark.getProperty('voices')
Mark.setProperty('voice',voice[0].id)

def speak(audio):
    print("Mark: " + audio)
    Mark.say(audio)
    Mark.runAndWait()

def covidGlobal():
    r = requests.get('https://api.covid19api.com/summary').json()
    data = r["Global"]
    date = datetime.datetime.now().date()
    t = ToastNotifier()
    text = f'Date: {date} \nNew Confirmed: {data["NewConfirmed"]} \nTotal Confirmed: {data["TotalConfirmed"]} \nNew Deaths: {data["NewDeaths"]} \nTotal Deaths: {data["TotalDeaths"]} \nNew Recovered: {data["NewRecovered"]} \nTotal Recovered: {data["TotalRecovered"]}'
    speak(text)
    t.show_toast("Covid 19 Update",text)

#speak("Hello sir")

def covidCountries(country):
    r = requests.get('https://api.covid19api.com/summary').json()
    date = datetime.datetime.now().date()
    data = r["Countries"]
    for i in range(len(data)):
        if country == data[i]["Slug"]:
            text = f'Date: {date} \nCountry: {data[i]["Country"]} \nNew Confirmed: {data[i]["NewConfirmed"]} \nTotal Confirmed: {data[i]["TotalConfirmed"]} \nNew Deaths: {data[i]["NewDeaths"]} \nTotal Deaths: {data[i]["TotalDeaths"]} \nNew Recovered: {data[i]["NewRecovered"]} \nTotal Recovered: {data[i]["TotalRecovered"]}'
            t=ToastNotifier()
            speak(text)
            t.show_toast("Covid 19 Update",text)

#def C19Country():
   # country = str(input("Enter command: ")).lower()#command().lower() #str(input("Enter command: ")).lower()
   # covidCountries(country)

def time():
    Now = datetime.datetime.now().strftime("%I:%M %p")
    speak("The time now is "+Now)

#Date()

def cmd():
    speak("How can i help you?")
    s = str(input("Kevin: ")).lower()
    return s

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour <= 12:
        speak("Good morning, sir")
    elif hour > 12 and hour <= 18:
        speak("Good afternoon, sir")
    elif hour > 18 and hour <= 21:
        speak("Good evening, sir")
    elif hour > 21 or hour < 5:
        speak("Good night, sir")
    covidGlobal()

def command():
    speak("How can i help you?")
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio,language="en")
        print("Kevin: " + str(query).capitalize())
    except sr.UnknownValueError:
        speak("Please repeat or typing the command")
        query=str(input("Your order is: "))
    return query

def searchGG():
    speak("What should i search, boss?")
    search = cmd()  #cmd()#command().lower()
    url=f"https://www.google.com/search?q={search}"
    wb.get().open(url)
    speak(f"Here is your {search} on Google")

def searchYT():
    speak("What should i search, boss?")
    search = cmd() #cmd()#command().lower()
    url=f"https://www.youtube.com//search?q={search}"
    wb.get().open(url)
    speak(f"Here is your {search} on Youtube")

def messenger():
    url=f"https://www.facebook.com/messages/t/4238110422943672"
    wb.get().open(url)
    speak(f"Here is your Messenger")

def fb():
    url=f"https://www.facebook.com/"
    wb.get().open(url)
    speak(f"Here is your Facebook")

def Music(music):
    m = f"F:\Bot\CreateBot-Git\CreateBot\Music\{music}.mp3"
    os.startfile(m)

def music():
    music = cmd()#command().lower() #cmd()
    Music(music)

if __name__ == "__main__":
    welcome()
    while True:
        query = cmd()#command().lower() #cmd()
        if "google" in query:
            searchGG()
        elif "youtube" in query:
            searchYT()
        elif "messenger" in query:
            messenger()
        # elif "open video" in query: # function Open video
        #     m = r""
        #     os.startfile(m)
        elif "time" in query:
            time()
        elif "facebook" in query:
            fb()
        elif "shut down" in query or "end" in query:
            speak("Goodbye, sir")
            exit()
        elif "covid" in query or "coronavirus" in query:
            speak("Which country do you wanna check?")
            s = cmd() #cmd() # command().lower()
            if "global" in s:
                covidGlobal()
            else:
                covidCountries(s)
        elif "music" in query:
            speak("Which song do you wanna listen to?")
            music()
        else:
            speak("I can't hear you, try again!!!")