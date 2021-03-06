import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


@app.route("/users_books/<username>")
def users_books(username):
    user_id = mongo.db.users.find_one({"username": username})["_id"]
    users_books = mongo.db.books.find({"created_by": username})

    return render_template("profile.html",
    user_id=user_id, users_books=users_books)


@app.route("/delete_user/<username>")
def delete_user(username):
    mongo.db.users.remove({"username": username})
    session.clear()

    flash("Your Profile Successfully Deleted")
    return redirect(url_for("register"))  


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password!")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if session.get('user'):
        if request.method == "POST":
            book = {
            "image_url": request.form.get("image_url"),
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "category_name": request.form.get("category_name"),
            "review_text": request.form.get("review_text"),
            "date_of_review": request.form.get("date_of_review"),
            "created_by": session["user"]
            }
            mongo.db.books.insert_one(book)
            flash("Book Review Successfully Added!")
            return redirect(url_for("get_books"))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add_book.html", categories=categories)

    flash("You must Register or Log In to add a book!")
    return redirect(url_for("register"))


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
           "image_url": request.form.get("image_url"),
           "title": request.form.get("title"),
           "author": request.form.get("author"),
           "category_name": request.form.get("category_name"),
           "review_text": request.form.get("review_text"),
           "date_of_review": request.form.get("date_of_review"),
           "created_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Review Successfully Updated")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_book.html", book=book, categories=categories)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Review Successfully Deleted")
    return redirect(url_for("get_books"))


@app.route("/get_categories")
def get_categories():
    if session.get('user'):
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("categories.html", categories=categories)
  
    flash("You must Register or Log In to manage categories!")
    return redirect(url_for("register"))


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if session.get('user'):
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(url_for("get_categories"))

        return render_template("add_category.html")

    flash("You must Register or Log in to add category!")
    return redirect(url_for("register"))    


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Succesfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
