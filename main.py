import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recogniser = sr.Recognizer
engine = pyttsx3.init()
newsapi = "a510f73a87b94282858df9ed11dfc36d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.musics[song]
        webbrowser.open(link)

    elif "news" in c.lower().startswith("tell news"):
        r = requests.get(f"GET https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # phrase the json articles
            data = r.json()

            # extract the articles
            articles = data.get('aricles',[])

            # print the headlines
            for article in articles:
                speak(article['title'])


if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
       #listen for the wake word "jarvis"
       # obtain audio from the microphone
       r = sr.Recognizer()


       print("recognizing....")
       try:
          with sr.Microphone() as source:
             print("Listening....")
             audio = r.listen(source,timeout=2,phrase_time_limit=1)
             word = r.recognize_google(audio)
             if(word.lower() == "jarvis"):
                 speak("ya")
                 #listen for command
                 with sr.Microphone() as source:
                     print("jarvis Active....")
                     audio = r.listen(source)
                     command = r.recognize_google(audio)

                     processcommand(command)
                     

       except Exception as e:
             print("Error; {0}".format(e))