from datetime import date, datetime
import speech_recognition
import pyttsx3
import wikipedia
import os
import subprocess
import playsound
import wolframalpha
import random
import webbrowser
import shutil
import time
import datetime
 	

robotEar = speech_recognition.Recognizer()													# robotEar: bien nhan am thanh
robotMouth = pyttsx3.init()																	# robotMoutth: bien phat am thanh
robotBrain = ""		

def speak(audio):
    robotMouth.say(audio)
    robotMouth.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = "Jarvis 1 point o"
    speak("I am your Assistant")
    speak(assname)


def takeCommand():

	r = speech_recognition.Recognizer()

	with speech_recognition.Microphone() as mic:
		r.adjust_for_ambient_noise(mic)
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(mic)
		# audio = r.record(mic, duration=5)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio)
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"

	return query

def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")
																		# robotBrain: bien nhan noi dung phan hoi lai
def openApp(name):								#hàm tìm đường dẫn và mở app
	appPath = ""
	for root, dirs, files in os.walk("C:\\"):
		if name in files:
			appPath = os.path.join(root, name)
	if(appPath):
		subprocess.call(appPath)
	else:
		global robotBrain
		robotBrain = "App not found"

if __name__ == "__main__":
	clear = lambda: os.system("cls")

	clear()
	wishMe()
	usrname()

	while True:
			# with speech_recognition.Microphone() as mic:		
			# 	robotEar.adjust_for_ambient_noise(mic)
			# 	print("robot: i'm listening")
			# 	#audio = robotEar.listen(mic)
			# 	audio = robotEar.record(mic, duration=5)
				
			# try:
			# 	you = robotEar.recognize_google(audio)
			# except:
			# 	you = ""
		# you = you.lower()								#lowercase input để dễ so sánh 
		# print("You: ", you)


		# you = takeCommand()
		you = input("Say something: ")
		
		if you == "":
			robotBrain = "Sorry, please say again"
		elif "can you hear me" in you:
			robotBrain = "Yes, very clearly"
		elif "hello" in you:
			robotBrain = "Hi, Master"
		elif "who are you" in you:
			robotBrain = "I am Corona, your assistant"
		elif "girlfriend" in you:
			robotBrain = "not yet, may be soon"
		elif "today" in you:
			today = date.today()
			robotBrain = today.strftime("%B %d, %Y")
		elif "time" in you:
			now = datetime.now()
			robotBrain = now.strftime("%H hours %M minutes %S seconds")
		elif "open" in you:
			if "notepad" in you:
				openApp("notepad.exe")
			elif "excel" in you:
				openApp("EXCEL.EXE")
			elif "powerpoint" in you:
				openApp("POWERPNT.EXE")
			elif "word" in you:
				openApp("WINWORD.EXE")
			elif "calculator" in you:
				openApp("calc.exe")
			elif "microsoft" in you and "edge" in you:
				openApp("msedge.exe")
			elif "chrome" in you:
				openApp("chrome.exe")
		elif "bye" in you:
			robotBrain = "Good bye, Toan"
			voices = robotMouth.getProperty('voices')  
			robotMouth.setProperty('voice', voices[1].id)  
		
			robotMouth.say(robotBrain)
			robotMouth.runAndWait()
			break
		elif "play music" in you or "play song" in you:
			speak("Here you go with music")
			# music_dir = "G:\\Song"
			cwd = os.getcwd()
			# music_dir = os.path.join(cwd,"\\music\\" )
			music_dir = cwd + "\\music\\"
			songs = os.listdir(music_dir)
			# print(songs)
			# mixer.init()
			# mixer.music.load(os.path.join(music_dir, songs[1]))
			# mixer.music.play()

			# random = os.startfile(os.path.join(music_dir, songs[1]))
			temp = random.randint(0, len(songs) - 1)
			playsound.playsound(os.path.join(music_dir, songs[temp]))

		elif "search" in you or "play" in you:

			you = you.replace("search", "")
			you = you.replace("play", "")
			webbrowser.open(you)

		elif "calculate" in you:

			app_id = "4EG49J-QU3XK7KPL3"
			client = wolframalpha.Client(app_id)
			indx = you.lower().split().index("calculate")
			you = you.split()[indx + 1 :]
			res = client.query(" ".join(you))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)
		#elif "what is" or "what are" or "who are" or "who is" in you:
		else:
			try:
				robotBrain = wikipedia.summary(you, sentences = 2)
			except:
				robotBrain = "Can't find " + you
		#else:
		#	robotBrain = "Don't give up, do your best and the rest will come"
		
		# print("RobotBrain: " + robotBrain)

		# voices = robotMouth.getProperty('voices')  
		# robotMouth.setProperty('voice', voices[1].id)  
		
		# robotMouth.say(robotBrain)
		# robotMouth.runAndWait()

