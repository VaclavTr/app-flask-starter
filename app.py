from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name=request.args.get("name")
	surname=request.args.get("surname")

	return render_template("page.html", date=date, name=name, surname=surname)

@app.route("/pozdrav-post", methods=["GET", "POST"])
def pozdrav_post():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name = request.form.get("name")
	surname = request.form.get("surname")
	password = request.form.get("password")
	message_name1= None
	message_name2 = None
	if not name or not surname:
		message_name1 = "ERROR: Zadej jméno a příjmení."
		name = None
		surname = None
	elif len(name) > 50 or len(surname) > 50:
		message_name2 = "ERROR: Jméno a příjmení musí mít maximálně 50 znaků."
		name = None
		surname = None
	message = None
	heslo = "SPRAVNE_HESLO"
	if not password:
		message=None
	elif password == heslo:
		message = "Správné heslo!"
	else:
		message = "ERROR: Chybné heslo!"
	return render_template("pozdrav_post.html", date=date, name=name, surname=surname, message=message, message_name1=message_name1, message_name2=message_name2)	
	

if __name__=="__main__":
	app.run(debug=True)