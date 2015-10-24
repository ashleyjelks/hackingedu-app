<<<<<<< HEAD
from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "MuchSecretWow"

@app.route('/')
def index(): 
	print "hey rosy did this work?"
	return render_template('index.html')

	if __name__ == "__main__": 
		app.debug = True
		app.run()


