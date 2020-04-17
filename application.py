# necessary imports

import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd, admin_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
sess = Session()
sess.init_app(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///readabook.db")


@app.route("/")
@login_required
def index():
    """Show user homapage"""
    rows = db.execute("SELECT * FROM Books")
    return render_template("index.html", books=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation password", 403)

        password = request.form.get("password")
        confirm = request.form.get("confirmation")

        if password != confirm:
            return apology("passwords do not match", 403)


        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if len(rows) != 0:
            return apology("username already taken", 403)

        hash_ = generate_password_hash(request.form.get("password"))

        rows = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash_)",
                          username=request.form.get("username"), hash_=hash_)
        return redirect("/login")

    else:
        return render_template('register.html')


@app.route("/books")
@login_required
def books():
    """List books"""
    rows = db.execute("SELECT * FROM Books")

    return render_template("books.html", books=rows)

@app.route("/book/<isbn>")
def book(isbn):
    """Book details"""
    row = db.execute("SELECT * FROM Books WHERE isbn=:isbn", isbn=isbn)
    return render_template("book_details.html", book=row[0])


@app.route("/borrow", methods=["GET", "POST"])
def borrow():
    """Allow request for available books"""
    if request.method == "POST":
        if not request.form.get("email"):
            return apology("Please enter Email address")
        elif not request.form.get("fullname"):
            return apology("Please enter Email address")
        elif not request.form.get("phoneNumber"):
            return apology("Please enter Email address")
        elif not request.form.get("bookTitle"):
            return apology("Please enter Email address")
        elif not request.form.get("postalAdd"):
            return apology("Please enter Email address")

    else:
        return render_template("borrow.html")

@app.route("/admin", methods=["GET", "POST"])
# @login_required
def admin():
    """Allow admin login"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM admins WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which admin has logged in
        session["admin_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/dashboard")
    else:
        return render_template("admin.html")

@app.route("/dashboard")
@admin_required
def dashboard():
    """Show admin homapage"""
    rows = db.execute("SELECT * FROM Books")
    return render_template("admin_index.html", books=rows)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
