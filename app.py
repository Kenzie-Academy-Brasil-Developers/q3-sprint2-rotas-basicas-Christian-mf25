from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route("/", methods=["GET"])
def name():
    person = {"data": "Hello Flask!"}
    return person


@app.route("/current_datetime", methods=["GET"])
def date_time():
	hour = datetime.now().strftime("%H")
	minutes = datetime.now().strftime("%M")
	seconds = datetime.now().strftime("%S")
	period = datetime.now().strftime("%P").upper()
	day = datetime.now().strftime("%d")
	month = datetime.now().strftime("%m")
	year = datetime.now().strftime("%Y")
	moment = ""
	date_time = f"{day}/{month}/{year} {hour}:{minutes}:{seconds} {period}"

	if int(hour) < 12:
		moment += "Bom dia!"
	elif int(hour) < 18:
		moment += "Boa tarde!"
	else:
		moment += "Boa noite!"
    
	result = {"current_datetime": date_time, "message": moment}

	return result