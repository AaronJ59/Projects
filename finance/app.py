import os
import datetime
import pytz
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    PURCHASES = []
    grand_total = 0

    stocks = db.execute(
        "SELECT stock_symbol, stock_price, shares FROM new_purchases WHERE user_id = ?",
        session["user_id"],
    )
    for stock in stocks:
        stock_info = lookup(stock["stock_symbol"])
        if stock_info:
            stock["stock_price"] = stock_info["price"]
            stock["total_value"] = stock["shares"] * stock["stock_price"]
            grand_total = grand_total + stock["total_value"]
            PURCHASES.append(stock)
    result = db.execute("SELECT cash FROM users WHERE id = ?", (session["user_id"],))
    cash = result[0]["cash"]
    grand_total = cash + grand_total

    return render_template(
        "index.html", purchases=PURCHASES, cash=cash, grand_total=grand_total
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        if not symbol:
            return apology("Symbol empty")
        symbol_info = lookup(symbol)
        if symbol_info == None:
            return apology("Symbol DNE")

        shares = request.form.get("shares")
        try:
            shares = int(shares)
        except ValueError:
            return apology("Invalid shares")

        if shares < 1:
            return apology("Shares must be a positive number")
        stock_current_price = symbol_info["price"]
        result = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = result[0]["cash"]
        date = datetime.datetime.now(pytz.timezone("US/Eastern"))
        if cash < stock_current_price * shares:
            return apology("Can't afford it")

        previous_purchase = db.execute(
            "SELECT * FROM new_purchases WHERE user_id = ? AND stock_symbol = ?",
            session["user_id"],
            symbol,
        )
        # if you own some shares of the stock you are trying to purchase
        if previous_purchase:
            # Calculate new total of shares
            new_shares = previous_purchase[0]["shares"] + shares
            # Update the existing row with the new total of shares
            db.execute(
                "UPDATE new_purchases SET shares = ?, stock_price = ?, date = ? WHERE user_id = ? AND stock_symbol = ?",
                new_shares,
                stock_current_price,
                date,
                session["user_id"],
                symbol,
            )
        else:
            # Insert new purchase record if no previous purchases found
            db.execute(
                "INSERT INTO new_purchases (user_id, stock_symbol, stock_price, shares, date) VALUES (?, ?, ?, ?, ?)",
                session["user_id"],
                symbol,
                stock_current_price,
                shares,
                date,
            )

        # Deduct the purchase amount from the user's cash
        cash = cash - (stock_current_price * shares)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        buy_or_sell = "buy"
        db.execute(
            "INSERT INTO history (user_id, stock_symbol, stock_price, shares, date, buy_or_sell) VALUES (?, ?, ?, ?, ?, ?)",
            session["user_id"],
            symbol,
            stock_current_price,
            shares,
            date,
            buy_or_sell,
        )

        flash(
            f"Bought {shares} of {symbol} for {usd(stock_current_price)}, Updated cash: {usd(cash)}"
        )

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    TRANSACTIONS = []

    history = db.execute("SELECT * FROM history WHERE user_id = ?", session["user_id"])
    for transaction in history:
        TRANSACTIONS.append(transaction)

    return render_template("history.html", transactions=TRANSACTIONS)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stock_sym = request.form.get("symbol")
        stock_info = lookup(stock_sym)
        if stock_info == None:
            return apology("Stock symbol doesn't exist")
        return render_template(
            "quoted.html", price=usd(stock_info["price"]), name=stock_info["symbol"]
        )
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        rows = db.execute("SELECT username FROM users")
        existing_usernames = [row["username"] for row in rows]
        new_username = request.form.get("username")
        new_password = request.form.get("password")
        if not new_username or new_username in existing_usernames:
            return apology("Username issue")
        if not new_password:
            return apology("No password")
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Password doesn't match or blank")
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            new_username,
            generate_password_hash(request.form.get("password")),
        )
        return render_template("login.html")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    STOCKS = []
    stock_symbols = db.execute(
        "SELECT DISTINCT stock_symbol FROM new_purchases WHERE user_id = ?",
        session["user_id"],
    )
    for stock in stock_symbols:
        STOCKS.append(stock["stock_symbol"])

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Didn't choose option")
        if not request.form.get("shares"):
            return apology("Didn't write shares")
        shares_count_list = db.execute(
            "SELECT SUM(shares) AS total_shares FROM new_purchases WHERE stock_symbol = ? AND user_id = ?",
            request.form.get("symbol"),
            session["user_id"],
        )
        total = shares_count_list[0]["total_shares"]
        if total < int(request.form.get("shares")):
            return apology("insufficient amount of shares")

        for _ in range(int(request.form.get("shares"))):
            stock_list = db.execute(
                "SELECT stock_price, shares, date FROM new_purchases WHERE stock_symbol = ? AND user_id = ?",
                request.form.get("symbol"),
                session["user_id"],
            )
            shares = stock_list[-1]["shares"]
            stock_info = lookup(request.form.get("symbol"))
            current_stock_price = stock_info["price"]
            date = stock_list[-1]["date"]

            if shares - 1 == 0:
                result = db.execute(
                    "SELECT cash FROM users WHERE id = ?", session["user_id"]
                )
                cash = float(result[0]["cash"])
                cash = cash + current_stock_price
                db.execute(
                    "UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"]
                )
                db.execute(
                    "DELETE FROM new_purchases WHERE date = ? AND user_id = ?",
                    date,
                    session["user_id"],
                )

            if shares > 1:
                result = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
                cash = float(result[0]["cash"])
                cash = cash + current_stock_price
                db.execute(
                    "UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"]
                )
                price_per_stock = current_stock_price
                shares = shares - 1
                db.execute(
                    "UPDATE new_purchases SET stock_price = ?, shares = ? WHERE user_id = ? AND date = ?",
                    price_per_stock,
                    shares,
                    session["user_id"],
                    date,
                )

        stock_info = lookup(request.form.get("symbol"))
        current_stock_price = stock_info["price"]
        date = datetime.datetime.now(pytz.timezone("US/Eastern"))
        buy_or_sell = "sell"
        db.execute(
            "INSERT INTO history (user_id, stock_symbol, stock_price, shares, date, buy_or_sell) VALUES (?, ?, ?, ?, ?, ?)",
            session["user_id"],
            request.form.get("symbol"),
            current_stock_price,
            request.form.get("shares"),
            date,
            buy_or_sell,
        )
        return redirect("/")

    else:
        return render_template("sell.html", stocks=STOCKS)
