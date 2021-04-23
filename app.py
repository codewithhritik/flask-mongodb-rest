# Essential Imports
import flask
from flask import jsonify, request
from mongoengine import *
from models import *

from flask_mongoengine import MongoEngine
db = MongoEngine()

app = flask.Flask(__name__)

# Configure the Database
app.config.from_pyfile('config.py')
#Initialise the Database
db.init_app(app)

# Add a book - Create
@app.route("/add_book", methods=["POST"])
def add_book():
    new_book = Book()

    params_data = flask.request.get_json()
    new_book.name = params_data.get('name')
    new_book.author = params_data.get('author')

    new_book.save()

    # return a jsonified object
    return flask.jsonify(new_book=new_book)

# Read all Books - Read
@app.route("/get_books", methods=["GET"])
def get_books():
    # Book.objects() gets us all the data from the database
    books = Book.objects()

    return flask.jsonify(books=books)

# Update a book - Update
@app.route("/update_book/<book_name>", methods=["PUT"])
def update_book(book_name):
    # Gets the book_name entered in the parameters
    book = Book.objects(name=book_name).first()

    params_data = flask.request.get_json()
    name = params_data.get('name')
    author = params_data.get('author')
    
    # Update the book with new data
    book.update(name=name, author=author)

    return flask.jsonify(book=book)

# Delete a Book - Delete
@app.route("/delete_book/<book_name>", methods=["DELETE"])
def delete_book(book_name):
    book = Book.objects(name=book_name).first()

    book.delete()

    return flask.jsonify(book=book)

if __name__ == '__main__':
    app.run(port=5000)