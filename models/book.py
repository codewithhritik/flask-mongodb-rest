from models import db

class Book(db.Document):
    name = db.StringField()
    author = db.StringField()