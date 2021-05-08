  
from flask import Flask, make_response, request, jsonify
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_route

app= Flask(__name__)
api = Api(app)

DB_ATLAS_URI = "mongodb+srv://cst_user:mcit123@cluster0.vo3fn.mongodb.net/mcit?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_ATLAS_URI

initialize_db(app)
initialize_route(api)

class Book(db.document):
	id = db.IntField()
	author = db. StringField()
	country = db.StringField()
	imageLink = db.StringField()
	language = db.StringField()
                   link = db.StringField()
	pages = db.IntField()
	title = db.StringField()
	year = db.IntField() 

	def to_json(self):
		return {
			"id" : self.id,
			"author": self.author,
			"country": self.country,
			"imageLink" : self.imageLink,
			"language": self.language,
			"link": self.link
			"pages" : self.pages,
			"title": self.title,
			"year": self.year
		}


@app.route('/api/db_populate', methods=['POST'])
def db_populate():
	book1 = Book(id=7, author = "unknown", country = "Canada", imageLink = "images/canadian.jpg", language = "English", link = "https://en.wikepedia.org/wiki/canada", pages = "50", title = "I Know", year = 1900)
	book1 = Book(id=8, author = "unknown", country = "USA", imageLink = "images/americann.jpg", language = "English", link = "https://en.wikepedia.org/wiki/american", pages = "500", title = "I am", year = 1970)
	pass
	book1.save()
	book2.save()
	return make_response("",201)

@app.route('/api/books', methods=['GET', 'POST'])
def api_books():
	if request.method = "GET":
		books = []
		for book in Book.objects:
			books.append(book)
		return make_response(jsonify(books), 200)
	elif request.method = "POST":
		content = request.json
		book = Book (id=content['id'], author=content['author], country=content['country'], imageLink=content['imageLinke'], language=content['language'], link=content['link'], pages=content['pages'], title=content['title'], year=content['year'])
		book.save()
		retutn make_response("", 201)

@app.route('/api/books/<id>', methods=['GET', 'PUT',  'DELETE'])
def api_each_book(id):
	if request.method = "GET"
		book_obj = Book.objects(id=id).first()
		if book_obj:
			return make_response(jsonify(book_obj.to_json()), 200)
		else:
			return make_response("", 404)
	elif request.method = "PUT"
		content = request.json
		book_obj = Book.objects(id=id).first()
		book_obj.update(author=content['author'], country=content['country'], imageLink=content['imageLinke'], language=content['language'], link=content['link'], pages=content['pages'], title=content['title'], year=content['year'])
		return make_response("", 204)
	elif request.method = "DELETE"
		book_obj = Book.objects(id=id).first()
		book_obj.delete()
		return make_response("")

if _name_ = '_main_':
app.run()