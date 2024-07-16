import requests
import wikipedia
import pywhatkit
import pyautogui
import speech_recognition as sr
import gtts
from gtts import gTTS
import os
import webbrowser
import smtplib
from email.message import EmailMessage

# Replace with your News API key
NEWS_API_KEY = 'YOUR_API_KEY'

# Replace with your email credentials
EMAIL_ADDRESS = 'your_email_address'
EMAIL_PASSWORD = 'your_email_password'

def find_my_ip():
    ip_address = requests.get('https://api.ipify.org').text
    return ip_address

def get_latest_news():
    news = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}').json()
    return news

def get_random_joke():
    joke = requests.get('https://official-joke-api.appspot.com/random_joke').json()
    return joke

def open_notepad():
    os.system('notepad.exe')

def open_discord():
    os.system('discord.exe')

def play_on_youtube(video):
    pywhatkit.playonyt(video)

def search_on_google(query):
    pywhatkit.search(query)

def send_email(receiver_address, subject, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = receiver_address

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()

def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(number, message)

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f'You said: {query}')
            return query
        except sr.UnknownValueError:
            print('Sorry, I didn\'t understand that.')
            return ''

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('start output.mp3')

def main():
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.')

        elif 'news' in query:
            news = get_latest_news()
            speak(f'Top news: {news["articles"][0]["title"]}.')

        elif 'joke' in query:
            joke = get_random_joke()
            speak(f'Here\'s a joke for you: {joke["setup"]} {joke["punchline"]}.')

        elif 'youtube' in query:
            speak('What do you want to play on Youtube?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'google' in query:
            speak('What do you want to search on Google?')
            query = take_user_input().lower()
            search_on_google(query)

        elif 'email' in query:
            speak('Who do you want to send an email to?')
            receiver_address = take_user_input().lower()
            speak('What is the subject of the email?')
            subject = take_user_input().lower()
            speak('What is the message of the email?')
            message = take_user_input().lower()
            send_email(receiver_address, subject, message)

        elif 'whatsapp' in query:
            speak('Who do you want to send a WhatsApp message to?')
            number = take_user_input().lower()
            speak('What is the message?')
            message = take_user_input().lower()
            send_whatsapp_message(number, message)

if __name__ == '__main__':
    main()                  
