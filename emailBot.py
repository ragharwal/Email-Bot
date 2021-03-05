import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('your email','your password')
    email = EmailMessage()
    email['From'] = 'your email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'name1': 'email1',
    'name2': 'email2',
    'name3': 'email3'
}
def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is subject of your email')
    subject = get_info()
    talk('Tell me the body of your email')
    message = get_info()
    send_email(receiver,subject,message)
    talk('Hey Raghav. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()
