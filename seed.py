from server import app
from flask_sqlalchemy import SQLAlchemy
from model import User, Session, Class, db, connect_to_db

def populate_users():
	users = [
			["Joel Burton", "joel@gmail.com", "password", "17607030246", 0],
			["Amanda Fuhrmann", "amanda@gmail.com", "password", "14152250220", 1],
			["Rosy Sanchez", "lolroci@gmail.com", "password", "17607030246", 1],
			["Ashley Jelks", "ashley@gmail.com", "password", "16466480603", 1]			
			]
	for user in users: 
		user = User(user_name=user[0], email=user[1], password=user[2], phone=user[3], tutor_id=user[4])
		db.session.add(user)
	db.session.commit()

def populate_classes(): 

	subjects = ["Math", "Science", "English", "History", "Social Studies", "Computer Science"]
	for subject in subjects: 
		subject = Class(subject=subject)
		db.session.add(subject)
	db.session.commit()
	pass

def populate_sessions(): 
	sessions = [
		[1, "Math", 2], 
		[2, "English", 2],
		[3, "Computer Science", 2],
		[1, "Math", 2],
		[2, "Social Studies", 3], 
		[3, "Math", 3], 
		[4, "Computer Science", 3],
		[2, "History", 3],

	]
	for session in sessions: 
		session = Session(hours=session[0], subject_class=session[1], user_id=session[2])
		db.session.add(session)
	db.session.commit()

	pass


if __name__ == "__main__":
	connect_to_db(app)
	populate_users()
	populate_classes()
	populate_sessions()


