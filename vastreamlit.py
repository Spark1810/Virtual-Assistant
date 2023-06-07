# ================================================ Importing libraries
import streamlit as st
import pyttsx3;
import time;
import mysql.connector;
import speech_recognition as sr;
import os
import pprint
from pprint import pprint
from gtts import gTTS
import pyttsx3;
from googletrans import Translator, constants
from pydub import AudioSegment
from pydub.silence import split_on_silence
import webbrowser
import datetime
import wikipedia
import requests
import pywintypes
from bs4 import BeautifulSoup
import win32gui, win32con
import os
import math
import numpy as np
import pandas as pd 
import random
import pyautogui
import pywhatkit
import datetime

#========================================== Voice funtion

def voice(txt):
    engine = pyttsx3.init();
    # Set Rate / speed
    engine.setProperty('rate', 150)
    #voices = engine.getProperty('voices')
    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    #engine.setProperty('voice', voices[sv].id)
    
    # Set Volume
    engine.setProperty('volume', 5.0)
    engine.say(txt);
    engine.runAndWait() ;

def response(text):
    # Method to self shut down system
    def quitSelf(self):
        elf.Speak("do u want to switch off the computer sir")
        # Input voice command
        take = st.text_input("Enter your command (yes or no) :")
        choice = take.lower()
        if choice == 'yes':
            # Shutting down
            st.write("Shutting down the computer")
            self.Speak("Shutting the computer")
            os.system("shutdown /s /t 30")
        else:
            # Idle
            st.write("Thank u sir")
            self.Speak("Thank u sir")
    def Speak(self, audio):
        # Constructor call for pyttsx3.init()
        engine = pyttsx3.init('sapi5')
        # Setting voice type and id
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()


    query = text.lower()
    if "open google" in query:
        voice("Opening Google ")
        webbrowser.open("www.google.com")

    elif "search wikipedia" in query:
        # if any one wants to have a information
        # from wikipedia
        voice("Checking the wikipedia ")
        query = query.replace("wikipedia", "")
        # it will give the summary of 4 lines from
        # wikipedia we can increase and decrease it also.
        result = wikipedia.summary(query, sentences=4)
        voice("According to wikipedia")
        voice(result)

    elif "close" in query and"tata" in query:
        voice("Bye. Have a great day"+z)
        st.write("Shut down initiating...")
        Maam = Gfg()
        Maam.quitSelf()
        
    elif "restart system" in query:
        voice("Bye. Have a great day"+z)
        st.write("Restart initiating...")
        Maam = Gfg2()
        Maam.quitSelf()

    elif "message" in query:
            voice("Please Enter The Message To Be Sent Sir")
            message=st.text_input("Please Enter The Message To Be Sent :")
            voice("Please Enter the number you wish to sent")
            cont=st.text_input("Please Enter the number you wish to sent :")
            current_time = datetime.datetime.now()
            # Add two minutes to the current tim
            scheduled_time = current_time + datetime.timedelta(minutes=2)
            # Convert the scheduled time to hours and minutes
            hours = scheduled_time.hour
            minutes = scheduled_time.minute
            if st.button('SEND'):
                st.write('SENDING THE MESSAGE...')
                # syntax: phone number with country code, message, hour and minutes
                pywhatkit.sendwhatmsg('+91'+cont, message, hours, minutes)

#----------------------------------------------------------------------

st.header('VIRTUAL ASSISTANT')
voice("Hello sir im TRIS your virtual assistant ! How can i help you today sir?")



def main():
    
    user_input = st.text_input("Enter your text :")
    if user_input:
        st.write("You entered:", user_input)
        response(user_input)

if __name__ == '__main__':
    main()
