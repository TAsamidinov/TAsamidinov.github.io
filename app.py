from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simy_dbte.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

@app.route("/tasamidinov.github.io/")
def index():
    return render_template("books.html", books=db.execute("SELECT * FROM books"))

@app.route("/tasamidinov.github.io/cart", methods = ["POST", "GET"])
def cart():
    if request.method == "POST":
        book_id = request.form.get("id")
        return redirect("/cart")

    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books = books)
