from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///my_db.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("tasamidinov.github.io/")
def index():
    return render_template("books.html", books=db.execute("SELECT * FROM books"))

@app.route("tasamidinov.github.io/cart", methods = ["POST", "GET"])
def cart():
    if "cart" not in session:
        session["cart"] = []

    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        return redirect("/cart")

    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books = books)
