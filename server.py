from flask import Flask, render_template
from jinja2 import StrictUndefined
import requests, json

app = Flask(__name__)

app.secret_key = "MuchSecretWow"
API_KEY = '1Kfdqvy6wHmvJ4LDyAVOl7saCBoKHcSb'

@app.route('/')
def index(): 
	url = "https://api.target.com/items/v3/"
	payload = {
			"product_id": "081-04-0231",
			"id_type": 'dpci', 
			"key": '1Kfdqvy6wHmvJ4LDyAVOl7saCBoKHcSb',
			}
	data = requests.get(url, params=payload)
	# data = json.loads(data.content)
	print "The data: ", data
	print "what you can do: ", data.content

	return render_template('index.html')

if __name__ == "__main__": 
	app.debug = True
	app.run()

@app.route('/register', methods=['POST'])
def process_registration():
	"""Registers new users"""

	email = request.form['email']
	user_name = request.form['username']
	password = request.form['password']
	phone = request.form['phone']
	tutor_id = request.form['tutor']

	new_user = User(email=email, user_name=user_name, password=password, phone=phone, tutor_id=tutor_id)

	old_email = User.query.filter(User.email == email).first()
	old_user_name = User.query.filter(User.user_name == user_name).first()

	if old_email is None and old_user_name is None:
		db.session.add(new_user)
		db.session.commit()

		user = User.query.filter(User.email == email).first()
		session["user_id"] = user.user_name
	else:
		flash("That Username or Email is already in use")
		return redirect('/register-form')

	flash('Welcome %s' % user_name)
	return redirect('/')
