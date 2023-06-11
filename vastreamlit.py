# ================================================ Importing libraries
import streamlit as st
import pyttsx3;
import time;
import mysql.connector;
import speech_recognition as sr;
import os
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
import screen_brightness_control as sbc
import win32gui, win32con
import os
import math
import numpy as np
import pandas as pd 
import random
import pyautogui
import pywhatkit
import datetime

z="sir"
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



def whether():
    st.write("Say the City Name...")
    city=""
        
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    
    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    
    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]
    
    # st.writeing all data
    st.write("Temperature is", temp)
    st.write("Time: ", time)
    st.write("Sky Description: ", sky)
    st.write(other_data)
    voice("Temperature is"+temp+" \n Sky Description: "+sky)

def decv():
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import math
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 10.0, None)
        volume.GetMasterVolumeLevel()

    except:
        st.write("Minimum Volume Attained "+z)
        voice("Minimum volume attained "+z)

def incv():
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import math
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb + 10.0, None)
        volume.GetMasterVolumeLevel()

    except:
        st.write("Maximum Volume Attained "+z)
        voice("Maximum volume attained "+z)

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

    elif "close" in query and "tata" in query:
        st.write("Closing the program!!!")
        time.sleep(2)
        voice("Bye. Have a great day")
        pyautogui.hotkey('ctrl', 'w')
        
        
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

    elif "who are you" in query:
        voice("Hello sir im TRIS your virtual assistant ! How can i help you today sir?")

    elif "climate" in query:
        whether()

    elif "open" in query:
            ap=query[4:]
            voice("opening "+ap)
            pyautogui.press("win")
            time.sleep(1)
            for i in ap:
                pyautogui.press(i)
            pyautogui.press('enter')

    elif "increase brightness" in query:
            for bri in sbc.get_brightness():
                if bri>90:
                    sbc.set_brightness(100)
                else:
                    sbc.set_brightness(bri+10)

    elif "decrease brightness" in query:
            for bri in sbc.get_brightness():
                if bri<10:
                    sbc.set_brightness(0)
                else:
                    sbc.set_brightness(bri-10)

    elif "increase volume" in query:
            incv()
            voice("Increased volume")

    elif "decrease volume" in query:
            decv()
            voice("Decreased volume")

    elif "fortune time" in query:
            st.write("Fortune Teller!!!")
            st.write("Say the Event...")
            voice("Say The Event"+z)
            a=st.text_input("Enter the Event :")
            if a:
                import random
                s=random.randint(1,8)
                if s==1:
                    st.write(a," will not happen in this lifetime!!!")
                    voice(a+" will not happen in this lifetime!!!")
                elif s==2:
                    st.write(a," will happen surely!!!")
                    voice(a+" will happen surely!!!")
                elif s==3:
                    st.write(a," will happen when you are 80 years!!!")
                    voice(a+" will happen when you are 80 years!!!")
                elif s==4:
                    st.write(a," may or may not happen!!!")
                    voice(a+" may or may not happen!!!")
                elif s==5:
                    st.write(a," will happen when you lose something which you like the most!!!")
                    voice(a+" will happen when you lose something which you like the most!!!")
                elif s==6:
                    st.write(a," can happen under gods grace!!!")
                    voice(a+" can happen under gods grace!!!")
                elif s==7:
                    st.write(a," will happen after a lot of struggle!!!")
                    voice(a+" will happen after a lot of struggle!!!")
                elif s==8:
                    st.write(a," will happen soon!!!")
                    voice(a+" will happen soon!!!")
                else:
                    st.write(a," will not happen!!!")
                    voice(a+" will not happen!!!")
            
            else:
                st.write("Please enter an event to check")
            time.sleep(3)
            st.write("Note: Future changes every second and this may or may not happen")

    elif "screenshot" in query:
            import pyscreenshot
            image = pyscreenshot.grab()
            image.show()

    elif "maximize" in query:
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MAXIMIZE)

    elif "minimise" in query:
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

    elif query !="":
        import os
        import openai
        openai.api_key = "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"
        def ask_chatgpt(prompt):
            model_engine = "text-davinci-003"
            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                ) 
            message = response.choices[0].text.strip()
            return message
        prompt =query
        response = ask_chatgpt(prompt)
        st.write("Tris :"+" "+response+" "+z)
        voice(""+" "+response+" "+z)
        
    

#----------------------------------------------------------------------

st.header('VIRTUAL ASSISTANT')




def main():
    
    user_input = st.text_input("Enter your text :")
    if user_input:
        st.write("You entered:", user_input)
        response(user_input)

if __name__ == '__main__':
    main()
