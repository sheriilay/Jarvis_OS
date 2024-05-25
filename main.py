import datetime
import subprocess
import pyjokes
import requests
import json
from PIL import Image, ImageGrab
from gtts import gTTS
from pynput import keyboard
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from playsound import playsound
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import smtplib
import openai
import base64


openai.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    """Speaks the given text."""
    engine.say(audio)
    engine.runAndWait()

def speak_news():
    """Reads out top headlines from The Times of Kazakhstan."""
    url = "http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=380bfd598de74ad6a1f13cd5daaf62bd"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]
    speak("Source: The Times Of Kazakhstan")
    speak("Today's Headlines are..")
    for index, article in enumerate(arts):
        speak(article["title"])
        if index == len(arts) - 1:
            break
        speak("Moving on to the next news headline..")
    speak("These were the top headlines, Have a nice day Sir!!..")

def sendEmail(to, content):
    """Sends an email using Gmail."""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("YOUR_EMAIL@gmail.com", "YOUR_PASSWORD")  # Replace with your actual email and password
    server.sendmail("YOUR_EMAIL@gmail.com", to, content)
    server.close()

def ask_gpt3(que):
    """Asks a question to GPT-3 and returns the answer."""
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Answer the following question: {que}\n",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    answer = response.choices[0].text.strip()
    return answer

def wishme():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis! How can I help you, sir?")

def takecommand(wake_word="jarvis, wake up"):
    """Listens for voice commands, activates on wake word."""
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for wake word...")
                audio = recognizer.listen(source)

                try:
                    wake_query = recognizer.recognize_google(audio, language="en-in").lower()
                    if wake_word in wake_query:
                        print("Wake word detected. Listening for command...")
                        speak("Yes, sir. What can I do for you?")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio, language="en-in")
                        print(f"User said: {command}\n")
                        return command.lower()
                    else:
                        print("Wake word not detected.")
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition; {e}")

            except KeyboardInterrupt:
                print("User interrupted. Exiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

def get_app(Q):
    """Handles user commands and performs actions."""
    if Q is None:
        print("No command received. Listening again...")
        return

    current = Controller()
    if Q == "time":
        x = datetime.datetime.now()
        speak(f"The current time is {x}")
    elif Q == "news":
        speak_news()
    elif Q == "open notepad":
        subprocess.call(["Notepad.exe"])
    elif Q == "open calculator":
        subprocess.call(["calc.exe"])
    elif Q == "open stikynot":
        subprocess.call(["StikyNot.exe"])
    elif Q == "open shell":
        subprocess.call(["powershell.exe"])
    elif Q == "open paint":
        subprocess.call(["paint.exe"])
    elif Q == "open cmd":
        subprocess.call(["cmd.exe"])
    elif Q == "open discord":
        subprocess.call(["discord.exe"])
    elif Q == "open browser":
        subprocess.call(["C:\\Program Files\\Internet Explorer\\iexplore.exe"])
    elif Q == "open youtube":
        webbrowser.open("https://www.youtube.com/")
    elif Q == "open google":
        webbrowser.open("https://www.google.com/")
    elif Q == "open github":
        webbrowser.open("https://github.com/")
    elif "search for" in Q:
        que = Q.replace("search for", "").strip()
        answer = ask_gpt3(que)
        speak(answer)
    elif Q == "email to other":
        try:
            speak("What should I say?")
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source)
            to = "example@gmail.com"
            content = recognizer.recognize_google(audio, language="en-in")
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry, I can't send the email.")
    elif Q == "take screenshot":
        snapshot = ImageGrab.grab()
        drive_letter = "C:\\"
        folder_name = r"downloaded-files"
        folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
        extension = ".jpg"
        folder_to_save_files = f"{drive_letter}{folder_name}{folder_time}{extension}"
        snapshot.save(folder_to_save_files)
        speak("Screenshot saved.")
    elif Q == "jokes":
        speak(pyjokes.get_joke())
    elif Q == "start recording":
        current.press(Key.cmd)
        current.press(Key.alt)
        current.press('r')
        current.release(Key.cmd)
        current.release(Key.alt)
        current.release('r')
        speak("Started recording. Just say stop recording to stop.")
    elif Q == "stop recording":
        current.press(Key.cmd)
        current.press(Key.alt)
        current.press('r')
        current.release(Key.cmd)
        current.release(Key.alt)
        current.release('r')
        speak("Stopped recording. Check your game bar folder for the video.")
    elif Q == "clip that":
        current.press(Key.cmd)
        current.press(Key.alt)
        current.press('g')
        current.release(Key.cmd)
        current.release(Key.alt)
        current.release('g')
        speak("Clipped. Check your game bar file for the video.")
    elif Q == "take a break":
        speak("Goodbye, sir. Have a great day!")
        exit()
    else:
        answer = ask_gpt3(Q)
        speak(answer)

if __name__ == "__main__":
    wishme()
    while True:
        Query = takecommand()
        get_app(Query)