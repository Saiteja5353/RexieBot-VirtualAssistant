import tkinter as tk
import speech_recognition as aa
import pyttsx3
import webbrowser
import sys
import pywhatkit
import threading
from PIL import Image, ImageTk
import datetime 
import time
import os
import wikipedia
import pyjokes
import PyPDF2
from tkinter import simpledialog, filedialog
import requests
from geopy.geocoders import Nominatim
import re

############################################# VOICE MODULATION ####################################
machine = pyttsx3.init()
rate = machine.getProperty('rate')
machine.setProperty('rate', 180)  # voice speed
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id) 

############################################## GUI SETUP #######################################
def gui_setup():
    file_path = r"D:\VS code partial\MINI PROJECT FINNAL\cat2.jpg"
    root = tk.Tk()
    root.title("Rexie- A Virtual Assistant")

    screen_width = root.winfo_screenwidth()# Set the size to fit the screen
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    root.configure(bg='black')# Set background color
    label = tk.Label(root, text="Rexie..", font=("Helvetica", 30), bg='yellow', fg='black', width=root.winfo_screenwidth(), height=1)
    label.pack(side="top", fill="x")

    try:  #image
        img = ImageTk.PhotoImage(Image.open(file_path))
        label = tk.Label(root, image=img, border=0)
        label.pack()
    except Exception as e:
        print(f"Error loading image: {e}")

    global label_var # Create a label variable after the root window is created
    label_var = tk.StringVar()
    label = tk.Label(root, textvariable=label_var, font=("Verdana", 22), wraplength=screen_width-100, fg='white', bg='black')  
    label.pack(pady=40)

    global search_var# Create a search bar
    search_var = tk.StringVar()
    search_entry = tk.Entry(root, textvariable=search_var, font=("Helvetica", 16), fg='black', bg='PaleGreen1', justify='center', width=50, border=10)
    search_entry.pack(pady=20)

    search_button = tk.Button(root, text="Search", command=search, font=("Helvetica", 14), fg='black', bg='skyblue', width=20) #search button
    search_button.pack(pady=10)

    Listen_button = tk.Button(root, text="Listen", command=Restart, font=("Helvetica", 14), fg='black', bg='pink', width=20) #listen button
    Listen_button.pack(pady=10)

    label = tk.Label(root, text="Developed by Saiteja and Chandrashekar   ", font=("Helvetica", 10), fg='white', bg='black', wraplength=screen_width-100)
    label.place(relx=1.0, rely=0.9, anchor='se') # at end
    global intro 
    intro=0

    # Start the Rexie function in a separate thread to keep listening
    threading.Thread(target=play_Rexie, daemon=True).start()

    root.mainloop()

######################################### RECOGNITION ################################################
def recognize_speech():
    listener = aa.Recognizer()
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            label_var.set("Listening... ")
            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(origin, duration=1)
            speech = listener.listen(origin, timeout=5, phrase_time_limit=5)

            print("Recognizing...")
            label_var.set("Recognizing... ")
            instruction = listener.recognize_google(speech)

            instruction = instruction.lower()
            print("Instruction:", instruction)
            return instruction

    except Exception as e:
        print(f"E:........... {e}")
        return "........."

######################################## SEARCH BAR ###############################################
def search():
    query = search_var.get()
    talk(query)
    webbrowser.open(f"https://www.google.com/search?q={query}")
    sys.exit()

######################################### LIISTEN BAR ################################################
def Restart():
    intro=1
    threading.Thread(target=play_Rexie,daemon=True).start()

######################################### TALK FUNCTION ################################################

def talk(text):  # speaks takes text as input
    try:
        machine.say(text)
        machine.runAndWait()
    except RuntimeError:
        pass  # Ignore the 'run loop already started' error

# def get_input(ask):
#     user_input = simpledialog.askstring("INPUT", ask)
#     return user_input

################################################ INSTRUCTIONS ##############################

def play_Rexie():
    global current_time 
    #current_time= datetime.datetime.now().strftime("%I:%M %p")
    current_time= datetime.datetime.now().strftime("%H:%M")
    print("Loading....")
    label_var.set("Loading....")
    time.sleep(3)
    if(int(current_time[0:2])<12):
        print("Good Morning Sir,Im Rexie ,a virtual Assistant developed by Sai teja and chandrashekhar")
        label_var.set("Good Morning Sir,Im Rexie,A Virtual Assistant developed by Saiteja and chandrashekhar")
        talk("Good Morning Sir,Im Rexie ,a virtual Assistant developed by Sai teja and chandrashekhar")
        time.sleep(1)
    else:
        print("Good Evening Sir,Im Rexie ,a virtual Assistant developed by Sai teja and chandrashekhar")
        label_var.set("Good Evening Sir,Im Rexie,A Virtual Assistant developed by Saiteja and chandrashekhar")
        talk("Good Evening Sir,Im Rexie ,a virtual Assistant developed by Sai teja and chandrashekhar")
        time.sleep(1)

    print("How can I help you")
    label_var.set("How can I help you")
    talk("How can I help you")
    time.sleep(1)
    while True:
        instruction = recognize_speech()
        command = "command :" + instruction
        label_var.set(command)
        time.sleep(1)
        numbers={"teja":"+9199999999999","chandu":"+9188888888888","Harshit":"+91666666666666"}

        apps={"notepad":"C:\\Users\\Saite\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe","brave":r"C:\Users\Saite\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe","firefox":r"C:\Users\Saite\AppData\Local\Mozilla Firefox\firefox.exe","vs code":r"C:\Users\Saite\AppData\Local\Programs\Microsoft VS Code\Code.exe"}

        if "open" in instruction and "youtube" in instruction:
            instruction = instruction.replace("open", "")
            instruction = instruction.replace("youtube", "")
            label_var.set("Opening YouTube... ")
            talk("Opening YouTube")
            if "search" in instruction:
                instruction = instruction.replace("search", "")
                pywhatkit.playonyt(instruction)
            else:
                label_var.set("What you want to watch on Youtube sir..")
                talk("What you want to watch on Youtube sir..")
                query = recognize_speech()
                time.sleep(1)
                if(query != "........."):
                    query = "query :" + query
                    label_var.set(query)
                    time.sleep(1)
                    pywhatkit.playonyt(query)
                else:
                    label_var.set("Unable to understand ..Opening Youtube")
                    webbrowser.open("https://youtube.com")
            break

        elif "alarm" in instruction:
            try:
                label_var.set("Say alarm time in HH:MM format")
                talk("Say alarm time in 24 Hours and minutes format")
                alarm_time=recognize_speech()
                print(alarm_time)
                integers = re.findall(r'\d+', alarm_time)

                if(int(integers[0])<9):hr="0"+str(integers[0]) 
                else:hr=str(integers[0])
                if(int(integers[1])<9):min="0"+str(integers[1]) 
                else:min=str(integers[1])

                alarm_time=hr+":"+min
                label_var.set(f"Setting alarm for {alarm_time}")
                talk(f"Setting alarm for {alarm_time}")
                while True:
                    current_time=datetime.datetime.now().strftime("%H:%M")
                    label_var.set(f"Alarm rings at {alarm_time}")
                    if current_time == alarm_time:
                        label_var.set("Time to wake up!")
                        i=0
                        while i<30:
                            talk("Time to wake up!")
                            time.sleep(1)
                            i=i+1
                        break
                    time.sleep(30)
            except Exception as e:
                    print(f"Unable to set {instruction}: {e}")
                    label_var.set(f"Unable to set{instruction}")
                    talk(f"Unable to set {instruction}")        
        

        elif ("search") in instruction or ("open wikipedia") in instruction:
            try:
                query = command.lower().replace('search', '').strip()
                wiki = wikipedia.summary(query, sentences=2)
                label_var.set("According to wikipedia")
                talk("According to wikipedia")
                label_var.set(wiki)
                talk(wiki)
                time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")
                label_var.set("Unable to understand")
                talk("Unable to understand")
                time.sleep(1)

        elif "shutdown the system" in instruction:
            print("Shutting down the System")
            label_var.set("Shutting down the System")
            talk("Shutting down the System")
            time.sleep(5)
            os.system('shutdown /s /t 5')

        elif "restart the system" in instruction:
            print("Restarting the System")
            label_var.set("Restarting the System")
            talk("Restarting the System")
            time.sleep(5)
            os.system('shutdown /r /t 5')


        elif "send" in instruction and "message" in instruction:
            instruction=list(instruction.split())
            person =instruction[len(instruction)-1] 
            label_var.set(f"Messaging to: {person}")
            talk(f"Messaging to: {person}")
            if person in numbers: 
                print("Please say message to send..")
                label_var.set("Please say message to send..")
                talk("Please say message to send..")
                msg=recognize_speech()
                label_var.set(f"message :{msg}")
                pywhatkit.sendwhatmsg(numbers[person],msg,int(current_time[0:2]),int(current_time[3:5])+2,15,True,1)
                time.sleep(100)
                print("msg is sent")
                label_var.set("msg is sent successfully")
                talk("msg is sent successfully")
            else:
                label_var.set("Unable to send mesage")
                talk("Unable to send message")

                

        elif "read pdf" in instruction:
            print("please select the pdf")
            label_var.set("please select the pdf")
            talk("please select the pdf")
            try:
                book = filedialog.askopenfilename()
                time.sleep(3)
                pdf = PyPDF2.PdfReader(book)
                pages = len(pdf.pages)
                label_var.set("Reading pdf")
                talk("Reading pdf")
                for pgno in range(0,pages):
                    pgno = int(pgno)
                    page = pdf.pages[pgno]  
                    text = page.extract_text()  
                    label_var.set(text)
                    talk(text)
            except Exception as e:
                print(f"Error: {e}")
                label_var.set("Sorry sir, something went wrong. Please check and retry")
                talk("Sorry sir, something went wrong. Please check and retry")
                time.sleep(1)
        
        elif "find my location" in instruction:
            print("wait sir,finding your location..")
            label_var.set("wait sir,finding your location..")
            talk("wait sir,finding your location..")
            try:
                response = requests.get('http://ip-api.com/json/')
                response.raise_for_status()  # Raise an exception for HTTP errors
                ip_info = response.json()

                if ip_info['status'] == 'success':
                    latitude = ip_info['lat']
                    longitude = ip_info['lon']

                    # Use geopy to get the address
                    geolocator = Nominatim(user_agent="geoapiExercises")
                    location = geolocator.reverse(f"{latitude}, {longitude}")

                    label_var.set(f" ip : {ip_info.get('ip')} \n city: {ip_info.get('city')}\n  state: {ip_info.get('region')}  \n country: {ip_info.get('country')} \n address: {location.address}")
                    talk(f" ip: {ip_info.get('ip')}  city: {ip_info.get('city')}  region: {ip_info.get('region')}   country: {ip_info.get('country')}  address: {location.address}")
                else:
                    label_var.set("Unable to get location")
                    talk("Unable to get location")

            except Exception as e:
                print (f"error: {str(e)}")
            
        elif "calculate" in instruction:
            print("please say mathematical statement sir")
            label_var.set("please say mathematical statement sir")
            talk("please say mathematical statement sir")

            try:
                state=recognize_speech()
                print(f"caluculating :{state}")
                label_var.set(f"caluculating :{state}")
                talk(f"caluculating :{state}")
                time.sleep(1)
                st=int(eval(state))
                
                if type(st)==int:
                    label_var.set(f"Answer is :{st}")
                    talk(f"Answer is :{st}")
                else:
                    label_var.set("Unable to calculate")
                    talk("Unable to calculate")

            except Exception as e:
                print (f"error: {str(e)}")


        elif "open google" in instruction:
            print("Opening Google")
            label_var.set("Opening Google... ")
            talk("Opening Google")
            time.sleep(1)
            print("What you want to search on Google sir..")
            label_var.set("What you want to search on Google sir..")
            talk("What you want to search on Google sir..")
            query = recognize_speech()
            if(query != "........."):
                qu = "query: " + query
                label_var.set(qu)
                time.sleep(1)
                webbrowser.open(f"https://google.com//search?q={query}")
            else:
                label_var.set("Unable to understand ..Opening Google")
                webbrowser.open("https://google.com")
            break



        elif "how are you" in instruction:
            print("I'm fine sir, what about you?")
            label_var.set("I'm fine sir, what about you?")
            talk("I'm fine sir, what about you?")
            time.sleep(1)
        elif "date" in instruction and "what" in instruction:
            today_date = datetime.datetime.now().strftime("%B %d, %Y")
            print("Sir, today is " + today_date)
            label_var.set("Sir, today's date is " + today_date)
            talk("Sir, today is " + today_date)
        elif "time" in instruction and "what " in instruction:
            print("Sir, the time is " + current_time)
            label_var.set("Sir, the time is " + current_time)
            talk("Sir, the time is " + current_time)
        elif "open" in instruction:
                try:
                    instruction=instruction.replace("open ","")
                    label_var.set(f"Opening {instruction}")
                    talk(f"Opening {instruction}")
                    if instruction in apps:
                        os.startfile(apps[instruction])
                        print(f"{instruction} opened successfully.")
                except Exception as e:
                    print(f"Failed to open {instruction}: {e}")
                    label_var.set(f"Failed to open {instruction}")
                    talk(f"Failed to open {instruction}")
                    
                            
            
        elif "close" in instruction:
            try:
                instruction=instruction.replace("close ","")
                label_var.set(f"Closing {instruction}")
                talk(f"Closing {instruction}")
                val=apps[instruction]
                if val=="vs code":
                    os.system(f"taskkill /f /im Code.exe")
                else:
                    le=len(val)-len(instruction)-4
                    print(val[le:])
                    if instruction in apps:
                        os.system(f"taskkill /f /im {val[le:]}")
                        print(f"{instruction} closed successfully.")
            except Exception as e:
                    print(f"Failed to close {instruction}: {e}")
                    label_var.set(f"Failed to close {instruction}")
                    talk(f"Failed to close {instruction}")

        elif "ok thanks" in instruction:
            label_var.set("Okay sir, you're welcome!")
            talk("Okay sir, you're welcome!")
            time.sleep(3)
            os.system(f"taskkill /f /im python.exe")
            sys.exit()


        elif  "sleep" and "seconds" in instruction:
            try:
                integers = re.findall(r'\d+', instruction)
                if(len(integers)==0):
                    time.sleep(180)
                else:
                    integers=int(integers[0])
                    label_var.set(f"Ok sir sleeping for {integers} seconds")
                    talk(f"Ok sir sleeping for {integers} seconds")
                    print("sleeping mode....")
                    time.sleep(integers)
                label_var.set("Hey,Im Back..!")
                talk("Hey,Im Back..!")
            except Exception as e:
                print(f"Error: {e}")
                label_var.set("Unable to understand")
                talk("Unable to understand")


        elif "tell me a joke" in instruction:
            joke = pyjokes.get_joke()
            label_var.set(joke)
            talk(joke)
            time.sleep(1)
        elif "hi" in instruction:
            label_var.set("Hi sir, I'm Rexie, a virtual Assistant")
            talk("Hi sir, I'm Rexie, a virtual Assistant")
            time.sleep(1)
            label_var.set("How can I help you..?")
            talk("How can I help you..?")
            time.sleep(1)
        else:
            print("Sorry sir, I'm unable to understand")
            label_var.set("Sorry sir, I'm unable to understand")
            talk("Sorry sir, I'm unable to understand")

if __name__ == "__main__":
    gui_setup()
