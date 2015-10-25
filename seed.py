from server import app
from flask_sqlalchemy import SQLAlchemy
from model import Class, db, connect_to_db

def populate_users():
	users = [
			["Amanda Fuhrmann", "amandafuhrmann@gmail.com", "password", "14152250220", None]
			["Rosy Sanchez", "lolroci@gmail.com", "password", "17607030246", None]
			
			]


def populate_classes(): 

	subjects = ["Math", "Science", "English", "History", "Social Studies", "Computer Science"]
	for subject in subjects: 
		subject = Class(subject=subject)
		db.session.add(subject)
	db.session.commit()
	pass

def populate_sessions(): 

	pass


if __name__ == "__main__":
	connect_to_db(app)
	# populate_classes()

