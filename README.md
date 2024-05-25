# Jarvis Voice-Controlled Personal Assistant
Project-work

Jarvis is a Python-based voice-controlled personal assistant designed to streamline everyday tasks using voice commands. It leverages various APIs and libraries to provide functionalities like retrieving news, sending emails, controlling applications, and more.

## Features
* Voice Recognition: Converts speech input to text using the speech_recognition library.
* Text-to-Speech: Provides spoken responses using pyttsx3.
* News Retrieval: Fetches and reads out the latest headlines from The Times of Kazakhstan.
* Email Sending: Sends emails via Gmail's SMTP server.
* Web Searches: Uses OpenAI's GPT-3 to answer questions and perform searches.
* Application Control: Launches and controls system applications.
* Web Browsing: Opens specific websites.
* Screenshot Capturing: Takes screenshots using Pillow.
* Joke Telling: Provides jokes using the pyjokes library.
* Screen Recording Control: Starts and stops screen recording using Windows Game Bar.

## Installation
Install Python: Download and install Python.

1. Install Required Libraries:

pip install speech_recognition pyttsx3 playsound datetime requests json pillow pynput openai pyjokes smtplib

2. Obtain and Configure API Keys:
  * OpenAI API Key from OpenAI.
  * The Times of Kazakhstan API Key from NewsAPI.
  * Gmail account credentials.
    

3. Set Environment Variables: Store your API keys and Gmail credentials in a .env file:

  OPENAI_API_KEY=your_openai_api_key
  
  NEWS_API_KEY=your_news_api_key
  
  GMAIL_ADDRESS=your_gmail_address
  
  GMAIL_PASSWORD=your_gmail_password
  
## Usage
Run the script and interact with Jarvis using voice commands:

python jarvis.py

Example Commands:

* "What's the time?"
* "Tell me the news"
* "Send an email to [email] with the content [message]"
* "Search for [query]"
* "Open Notepad"
* "Take a screenshot"
* "Tell me a joke"
