from flask import Flask, render_template, request
from datetime import date, datetime
import wikipedia
import os
import subprocess
import wolframalpha

def openApp(name):								#hàm tìm đường dẫn và mở app
	appPath = ""
	for root, dirs, files in os.walk("C:\\"):
		if name in files:
			appPath = os.path.join(root, name)
	""" if(appPath):
		subprocess.call(appPath)
	else:
		global robotBrain
		robotBrain = "App not found" """
	print(appPath)
	try:
		subprocess.call(appPath)
	except:
		global robotBrain
		robotBrain = "App not found"

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    robotBrain = ""
    if "hello" in userText:
	    robotBrain = "Hi, Master. How can i help you?"
    elif "who are you" in userText:
	    robotBrain = "I am Corona, your assistant"
    elif "girlfriend" in userText:
	    robotBrain = "not yet, may be soon"
    elif "today" in userText:
	    today = date.today()
	    robotBrain = today.strftime("%B %d, %Y")
    elif "time" in userText:
	    now = datetime.now()
	    robotBrain = now.strftime("%H hours %M minutes %S seconds")
    elif "open" in userText:
	    if "notepad" in userText:
		    openApp("notepad.exe")
	    elif "excel" in userText:
		    openApp("EXCEL.EXE")
	    elif "powerpoint" in userText:
		    openApp("POWERPNT.EXE")
	    elif "word" in userText:
		    openApp("WINWORD.EXE")
	    elif "calculator" in userText:
		    openApp("calc.exe")
	    elif "microsoft" in userText and "edge" in userText:
		    openApp("msedge.exe")
	    elif "chrome" in userText:
		    openApp("chrome.exe")
	    elif "garena" in userText:
		    openApp("Garena.exe")
    elif "bye" in userText:
	        robotBrain = "Good bye, Toan"
    elif "calculate" in userText:
        app_id = "4EG49J-QU3XK7KPL3"
        client = wolframalpha.Client(app_id)
        indx = userText.lower().split().index("calculate")
        tempText = userText.split()[indx + 1 :]
        res = client.query(" ".join(userText))
        robotBrain = next(res.results).text
		#elif "what is" or "what are" or "who are" or "who is" in userText:
    else:
	    try:
		    robotBrain = wikipedia.summary(userText, sentences = 2)
	    except:
		    robotBrain = "Can't find " + userText
		#else:
		#	robotBrain = "Don't give up, do userTextr best and the rest will come"
		
		# print("RobotBrain: " + robotBrain)

		# voices = robotMouth.getProperty('voices')  
		# robotMouth.setProperty('voice', voices[1].id)  
		
		# robotMouth.say(robotBrain)
		# robotMouth.runAndWait()
    return robotBrain

if __name__ == "__main__":
    app.run() 