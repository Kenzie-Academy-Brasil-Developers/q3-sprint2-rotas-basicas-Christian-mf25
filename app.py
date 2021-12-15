from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route("/", methods=["GET"])
def name():
    person = {"data": "Hello Flask!"}
    return person


@app.route("/current_datetime", methods=["GET"])
def date_time():
	date = datetime.now().strftime("%d/%m/%Y %H:%M:%S %P").upper()
	hour = datetime.now().strftime("%H")

	if int(hour) < 12:
		moment = "Bom dia!"
	elif int(hour) < 18:
		moment = "Boa tarde!"
	else:
		moment = "Boa noite!"
    
	result = {"current_datetime": date, "message": moment}

	return result
