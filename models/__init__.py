from flask_mongoengine import MongoEngine

db = MongoEngine()

from .book import Book
