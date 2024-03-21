import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import datetime
import requests
from wikipedia import wikipedia
# import weather_api
import pyjokes

api_key = "89f893c3e78bcbd44298e827ea567da4"

"""
api_key = "89f893c3e78bcbd44298e827ea567da4"
base_url = "http://api.weatherstack.com/"
params = {
    "q": "Pune,IN",  # Replace with the city and country code you want to query
    "units": "metric",  # You can choose 'imperial' or 'metric' for temperature units
    "appid": api_key
}
response = requests.get(base_url, params=params)
if response.status_code == 200:
    data = response.json()
    # Process the data as needed, e.g., extract and display the current temperature
    temperature = data["main"]["temp"]
    print(f"Current temperature: {temperature}°C")
else:
    print("Failed to retrieve weather data.")
"""
'''def ai(prompt):
    openai.api_key = apikey

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temprature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0

    )

    print(response[0]["text"]) '''


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print(text)


'''
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        say("Good Morning!")


    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        say("Good Afternoon!")

    else:
        print("Good Evening!")
        say("Good Evening!")

    say("I am Bro . Please tell me how may I help you")
'''


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        # Comment out the recognition part for testing
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        return "Some error occurred. Sorry from Jarvis"


def handle_command(query):
    if "give me a joke" in query.lower():
        joke = pyjokes.get_joke()
        print(joke)
        say(joke)


if __name__ == '__main__':
    print('PyCharm')
    say("hello I am BRO")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["wikipedia", "https://wikipedia.com"],
                 ["google", "https://google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir")
                webbrowser.open(site[1])
                # say(query)
        if 'open' in query:
            if query[0:4] == "open":
                query = query[5:]
                Result = webbrowser.open(query + ".com")
        if "open music" in query:
            musicPath = "C:/Users/Jaydeep Jare/Downloads/downfall-21371.mp3"
            os.startfile(musicPath)

        if "hello" in query.lower():
            say("Hello! How can I assist you?")

        if "the time" in query:
            musicPath = "C:/Users/Jaydeep Jare/Downloads/downfall-21371.mp3"
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        if "open youtube".lower() in query.lower():
            youtubePath = "C:/Users/Jaydeep Jare/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/YouTube.lnk"
            # os.startfile(f"open C:/Users/Jaydeep Jare/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/YouTube.lnk")
            os.startfile(youtubePath)

        if 'wikipedia' in query:
            pyttsx3.speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            say("According to wikipedia")
            say(results)
        elif 'who are you' in query:
            say("I am BRO, an A.I. voice model")
        elif 'open youtube' in query:
            say("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            say("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            say("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            say("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            say("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            say("opening whatsapp")
            webbrowser.open("web.whatsapp.com")
        elif 'play music' in query:
            say("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            say("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            say("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            say("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            say("opening local disk E")
            webbrowser.open("E://")
        elif 'what is' in query:
            Result = webbrowser.open("https://www.google.com/search?q=" + query)
        elif 'tell me' in query:
            say('Searching Internet...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            say("According to Internet")
            print(results)
            say(results)
        elif 'bye' in query:
            say("See you later. aligator")
            print("See you later!!!")
            exit(0)
        elif 'sleep' in query:
            exit(0)

'''
def respond_to_command(command):
    if command is not None:
        if "hello" in command.lower():
            say("Hello! How can I assist you?")
        elif "how are you" in command.lower():
            say("I'm just a computer program, but I'm doing well. How can I help?")
        else:
            say("I'm not sure how to respond to that.")
'''
