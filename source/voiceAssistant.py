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
import requests
from bs4.element import TemplateString
from bs4 import BeautifulSoup
from unidecode import unidecode







robotEar = speech_recognition.Recognizer()					# robotEar: bien nhan am thanh
robotMouth = pyttsx3.init()									# robotMoutth: bien phat am thanh
robotBrain = ""

def speak(audio):
	voices = robotMouth.getProperty('voices')
	robotMouth.setProperty('voice', voices[1].id)
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

	assname = "Corona SarsCo V 2"
	speak("I am your Assistant")
	speak(assname)

def takeCommand():

	#robotEar = speech_recognition.Recognizer()

	with speech_recognition.Microphone() as mic:
		robotEar.adjust_for_ambient_noise(mic)
		print("Listening...")
		robotEar.pause_threshold = 1
		#audio = robotEar.listen(mic)
		audio = robotEar.record(mic, duration=5)

	try:
		print("Recognizing...")
		query = robotEar.recognize_google(audio)
		print(f"User said: {query}\n")

	#except Exception as e:
		# print(e)
		# print("Unable to Recognize your voice.")
		# return "None"
	except:
		query = ""
	return query.lower()

def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Master")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")
																		

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

def searchWiki(keyWord):
	res = ""
	try:
		res = wikipedia.summary(keyWord, sentences = 2)
	except:
		res = "Can't find " + keyWord
	return res

def getWeather(str):
	place = str.split("weather")[1]
	search = f"temperature{place}"
	url = f"https://www.google.com/search?q={search}"
	r = requests.get(url)
	data = BeautifulSoup(r.text, "html.parser")
	temp = data.find("div",class_="BNeawe").text
	return temp

def getNews():
	#import what we need
	from requests_html import HTMLSession
	session = HTMLSession()
	#use session to get the page
	r = session.get('https://news.google.com/topstories?hl=vi&gl=VN&ceid=VN%3Avi')
	#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
	r.html.render(sleep=1, scrolldown=0)
	#find all the articles by using inspect element and create blank list
	articles = r.html.find('article')
	newslist = []
	#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
	for item in articles:
	    try:
	        newsitem = item.find('h3', first=True)
	        title = newsitem.text
	        link = newsitem.absolute_links
	        newsarticle = {
	            'title': unidecode(title),
	            'link': link 
	        }
	        newslist.append(unidecode(title))
	    except:
	       pass
	#print the length of the list
	for i in range(5):
	    print(newslist[i], end = '\n')






if __name__ == "__main__":
	clear = lambda: os.system("cls")

	clear()									# clear old command
	wishMe()								# introduce
	usrname()

	while True:
		
		you = takeCommand()
		#you = input("Say something: ")
		
		if you == "":
			robotBrain = "Sorry, please say again"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "bye" in you:
			robotBrain = "Good bye, Master"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
			break
		elif "can you hear me" in you:
			robotBrain = "Yes, very clearly"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "corona" in you:
			robotBrain = "yes, master. I'm here"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "hello" in you:
			robotBrain = "Hi, Master"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "hi" in you:
			robotBrain = "Hi, Master"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "who are you" in you:
			robotBrain = "I am Corona, your assistant"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "girlfriend" in you:
			robotBrain = "not yet, may be soon"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "today" in you:
			today = date.today()
			robotBrain = "today is " + today.strftime("%B %d, %Y")
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "time" in you:
			now = datetime.datetime.now()
			robotBrain = "it is " + now.strftime("%H hours %M minutes %S seconds")
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
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
		
		elif "play music" in you or "play song" in you:
			speak("Here you go with music")
			cwd = os.getcwd()
			music_dir = cwd + "\\music\\"
			songs = os.listdir(music_dir)
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
		elif "weather" in you:
			robotBrain = "The weather is: " + getWeather(you)
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "news" in you:
			robotBrain = "Here's you news"
			getNews()

		elif "wikipedia" in you:
			you = you.replace("wikipedia", "")
			robotBrain = searchWiki(you)
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif 'what is' in you:
			you = you.replace("what is ", "")
			robotBrain = searchWiki(you)
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "what are" in you:
			you = you.replace("what are ", "")
			robotBrain = searchWiki(you)
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "who are" in you:
			you = you.replace("who are ", "")
			robotBrain = searchWiki(you)
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		elif "who is" in you:
			you = you.replace("who is ", "")
			robotBrain = searchWiki(you)
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)

		else:
			robotBrain = "Sorry, try again. Don't give up, do your best and the rest will come"
			print("RobotBrain: " + robotBrain)
			speak(robotBrain)
		

	# exit program
