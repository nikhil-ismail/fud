import os
import re

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[fud]'

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():

    if request.method == "GET":
        return render_template("index.html")

@app.route("/junzi", methods=["GET", "POST"])
@login_required
def junzi():

    if request.method == "GET":
        id = 1
        menus = db.session.execute("SELECT * FROM product WHERE restaurant_id = ?", id)
        return render_template("junzi.html", menus = menus)

    elif request.method == "POST":
        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/junzi")

            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Junzi Kitchen'")
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/junzi")

        elif request.form.get("favbutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            rows = db.session.execute("SELECT * FROM fav WHERE product_id = ?", product)


            if rows:
                rowsuser = rows[0]["user_id"]
                rowsprod = rows[0]["product_id"]

                if rowsprod == product and rowsuser == session["user_id"]:
                    flash("Item Already In Favourites")
                    return redirect("/junzi")

            else:
                restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Junzi Kitchen'")
                restaurant = restaurant_dict[0]["id"]

                productname = request.form.get("productname")
                productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
                product = productdict[0]["id"]

                db.session.execute("INSERT INTO fav (user_id, restaurant_id, product_id) VALUES (?, ?, ?)", session["user_id"], restaurant, product)

                restaurantname = db.session.execute("SELECT name FROM restaurants WHERE id = ? ", restaurant)
                productname = db.session.execute("SELECT name FROM product WHERE id =?", product)

                flash("Item Added to Favourites!")
                return redirect("/junzi")


@app.route("/ashleys", methods=["GET", "POST"])
@login_required
def ashleys():

    if request.method == "GET":
        id = 2
        menus = db.session.execute("SELECT * FROM product WHERE restaurant_id = ?", id)
        return render_template("ashleys.html", menus = menus)

    elif request.method == "POST":
        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/ashleys")

            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Ashleys'")
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/ashleys")

        elif request.form.get("favbutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            rows = db.session.execute("SELECT * FROM fav WHERE product_id = ?", product)


            if rows:
                rowsuser = rows[0]["user_id"]
                rowsprod = rows[0]["product_id"]

                if rowsprod == product and rowsuser == session["user_id"]:
                    flash("Item Already In Favourites")
                    return redirect("/ashleys")

            else:
                restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Ashleys'")
                restaurant = restaurant_dict[0]["id"]

                productname = request.form.get("productname")
                productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
                product = productdict[0]["id"]

                db.session.execute("INSERT INTO fav (user_id, restaurant_id, product_id) VALUES (?, ?, ?)", session["user_id"], restaurant, product)

                restaurantname = db.session.execute("SELECT name FROM restaurants WHERE id = ? ", restaurant)
                productname = db.session.execute("SELECT name FROM product WHERE id =?", product)

                flash("Item Added to Favourites!")
                return redirect("/ashleys")


@app.route("/tropical", methods=["GET", "POST"])
@login_required
def tropical():

    if request.method == "GET":
        id = 3
        menus = db.session.execute("SELECT * FROM product WHERE restaurant_id = ?", id)
        return render_template("tropical.html", menus = menus)

    elif request.method == "POST":
        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/tropical")

            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Tropical Smoothie'")
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/tropical")

        elif request.form.get("favbutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            rows = db.session.execute("SELECT * FROM fav WHERE product_id = ?", product)


            if rows:
                rowsuser = rows[0]["user_id"]
                rowsprod = rows[0]["product_id"]

                if rowsprod == product and rowsuser == session["user_id"]:
                    flash("Item Already In Favourites")
                    return redirect("/tropical")

            else:
                restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Tropical Smoothie'")
                restaurant = restaurant_dict[0]["id"]

                productname = request.form.get("productname")
                productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
                product = productdict[0]["id"]

                db.session.execute("INSERT INTO fav (user_id, restaurant_id, product_id) VALUES (?, ?, ?)", session["user_id"], restaurant, product)

                restaurantname = db.session.execute("SELECT name FROM restaurants WHERE id = ? ", restaurant)
                productname = db.session.execute("SELECT name FROM product WHERE id =?", product)

                flash("Item Added to Favourites!")
                return redirect("/tropical")


@app.route("/salsa", methods=["GET", "POST"])
@login_required
def salsa():

    if request.method == "GET":
        id = 4
        menus = db.session.execute("SELECT * FROM product WHERE restaurant_id = ?", id)
        return render_template("salsa.html", menus = menus)

    elif request.method == "POST":
        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/salsa")

            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Salsa Fresca'")
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/salsa")

        elif request.form.get("favbutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            rows = db.session.execute("SELECT * FROM fav WHERE product_id = ?", product)


            if rows:
                rowsuser = rows[0]["user_id"]
                rowsprod = rows[0]["product_id"]

                if rowsprod == product and rowsuser == session["user_id"]:
                    flash("Item Already In Favourites")
                    return redirect("/salsa")

            else:
                restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Salsa Fresca'")
                restaurant = restaurant_dict[0]["id"]

                productname = request.form.get("productname")
                productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
                product = productdict[0]["id"]

                db.session.execute("INSERT INTO fav (user_id, restaurant_id, product_id) VALUES (?, ?, ?)", session["user_id"], restaurant, product)

                restaurantname = db.session.execute("SELECT name FROM restaurants WHERE id = ? ", restaurant)
                productname = db.session.execute("SELECT name FROM product WHERE id =?", product)

                flash("Item Added to Favourites!")
                return redirect("/salsa")




@app.route("/juice", methods=["GET", "POST"])
@login_required
def juice():

    if request.method == "GET":
        id = 5
        menus = db.session.execute("SELECT * FROM product WHERE restaurant_id = ?", id)
        return render_template("juice.html", menus = menus)

    elif request.method == "POST":
        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/juice")

            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Juice Box'")
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/juice")

        elif request.form.get("favbutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            rows = db.session.execute("SELECT * FROM fav WHERE product_id = ?", product)


            if rows:
                rowsuser = rows[0]["user_id"]
                rowsprod = rows[0]["product_id"]

                if rowsprod == product and rowsuser == session["user_id"]:
                    flash("Item Already In Favourites")
                    return redirect("/juice")

            else:
                restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Juice Box'")
                restaurant = restaurant_dict[0]["id"]

                productname = request.form.get("productname")
                productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
                product = productdict[0]["id"]

                db.session.execute("INSERT INTO fav (user_id, restaurant_id, product_id) VALUES (?, ?, ?)", session["user_id"], restaurant, product)

                restaurantname = db.session.execute("SELECT name FROM restaurants WHERE id = ? ", restaurant)
                productname = db.session.execute("SELECT name FROM product WHERE id =?", product)

                flash("Item Added to Favourites!")
                return redirect("/juice")


@app.route("/insomnia", methods=["GET", "POST"])
@login_required
def insomnia():

    if request.method == "GET":
        id = 6
        menus = db.session.execute("SELECT * FROM product WHERE restaurant_id = ?", id)
        return render_template("insomnia.html", menus = menus)

    elif request.method == "POST":
        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/insomnia")

            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Insomnia Cookies'")
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/insomnia")

        elif request.form.get("favbutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            rows = db.session.execute("SELECT * FROM fav WHERE product_id = ?", product)


            if rows:
                rowsuser = rows[0]["user_id"]
                rowsprod = rows[0]["product_id"]

                if rowsprod == product and rowsuser == session["user_id"]:
                    flash("Item Already In Favourites")
                    return redirect("/insomnia")

            else:
                restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Insomnia Cookies'")
                restaurant = restaurant_dict[0]["id"]

                productname = request.form.get("productname")
                productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
                product = productdict[0]["id"]

                db.session.execute("INSERT INTO fav (user_id, restaurant_id, product_id) VALUES (?, ?, ?)", session["user_id"], restaurant, product)

                restaurantname = db.session.execute("SELECT name FROM restaurants WHERE id = ? ", restaurant)
                productname = db.session.execute("SELECT name FROM product WHERE id =?", product)

                flash("Item Added to Favourites!")
                return redirect("/insomnia")

@app.route("/tarry", methods=["GET", "POST"])
@login_required
def tarry():

    if request.method == "GET":
        id = 7
        menus = db.session.execute("SELECT * FROM product WHERE restaurant_id = ?", id)
        return render_template("tarry.html", menus = menus)

    elif request.method == "POST":
        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/tarry")

            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Tarry Lodge'")
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/tarry")

        elif request.form.get("favbutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            rows = db.session.execute("SELECT * FROM fav WHERE product_id = ?", product)


            if rows:
                rowsuser = rows[0]["user_id"]
                rowsprod = rows[0]["product_id"]

                if rowsprod == product and rowsuser == session["user_id"]:
                    flash("Item Already In Favourites")
                    return redirect("/tarry")

            else:
                restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = 'Tarry Lodge'")
                restaurant = restaurant_dict[0]["id"]

                productname = request.form.get("productname")
                productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
                product = productdict[0]["id"]

                db.session.execute("INSERT INTO fav (user_id, restaurant_id, product_id) VALUES (?, ?, ?)", session["user_id"], restaurant, product)

                restaurantname = db.session.execute("SELECT name FROM restaurants WHERE id = ? ", restaurant)
                productname = db.session.execute("SELECT name FROM product WHERE id =?", product)

                flash("Item Added to Favourites!")
                return redirect("/tarry")

@app.route("/fav", methods=["GET", "POST"])
@login_required
def fav():

    if request.method == "GET":

        favs = db.session.execute("SELECT restaurant_id, product_id FROM fav WHERE user_id = ?", session["user_id"])

        for fav in favs:
            resname = db.session.execute("SELECT name FROM restaurants WHERE id = ?", fav["restaurant_id"])
            prodname = db.session.execute("SELECT name FROM product WHERE id = ?", fav["product_id"])
            fav["resname"] = resname[0]["name"]
            fav["prodname"] = prodname[0]["name"]


        return render_template("fav.html", favs = favs)

    elif request.method == "POST":
        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/fav")

            restaurantname = request.form.get("restaurantname")
            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = ?", restaurantname)
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/fav")

        elif request.form.get("removebutton"):

            #restaurantname = request.form.get("restaurantname")
            #restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = ?", restaurantname)
            #restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            db.session.execute("DELETE FROM fav WHERE product_id = ?", product)

            flash("Item Removed From Favourites!")
            return redirect("/fav")


@app.route("/rec", methods=["GET", "POST"])
@login_required
def rec():

    if request.method == "GET":
        recs = db.session.execute("SELECT * FROM rec WHERE user_id = ?", session["user_id"])

        for rec in recs:
            sender = rec["sender_id"]
            restaurant = rec["restaurant_id"]
            product = rec["product_id"]

            recsender = db.session.execute("SELECT name FROM users WHERE id = ?", sender)
            recres = db.session.execute("SELECT name FROM restaurants WHERE id = ?", restaurant)
            recprod = db.session.execute("SELECT name FROM product WHERE id = ?", product)

            rec["recsender"] = recsender[0]["name"]
            rec["recres"] = recres[0]["name"]
            rec["recprod"] = recprod[0]["name"]

        return render_template("rec.html", recs = recs)

    if request.method == "POST":

        if request.form.get("recbutton"):

            if not request.form.get("sender_name"):
                flash("Must Provide Your Full Name")
                return render_template("rec.html")

            if not request.form.get("receiver_name"):
                flash("Must Provide Your Friend's Full Name")
                return render_template("rec.html")

            rows = db.session.execute("SELECT * FROM users WHERE name = ?", request.form.get("receiver_name"))

            if len(rows) != 1:
                flash("Reccomendation Unsuccessful. Make Sure Your Friend Is Registered")
                return render_template("rec.html")

            if not request.form.get("restaurant"):
                flash("Must Provide A Restaurant")
                return render_template("rec.html")

            rows2 = db.session.execute("SELECT * FROM restaurants WHERE name = ?", request.form.get("restaurant"))

            if len(rows2) != 1:
                flash("Must Provide A Valid Restaurant")
                return render_template("rec.html")

            rows3 = db.session.execute("SELECT * FROM product WHERE name = ?", request.form.get("item"))

            if len(rows3) != 1:
                flash("Must Provide A Valid Item")
                return render_template("rec.html")

            restaurant_id = db.session.execute("SELECT id FROM restaurants WHERE name = ?", request.form.get("restaurant"))[0]["id"]
            print(restaurant_id)
            rows4 = db.session.execute("SELECT * FROM product WHERE restaurant_id = ? AND name = ?", restaurant_id, request.form.get("item"))

            if len(rows4) != 1:
                flash("Must Provide Item From Restaurant's Menu")
                return render_template("rec.html")

            product = db.session.execute("SELECT id FROM product WHERE name = ?", request.form.get("item"))[0]["id"]
            receiver = db.session.execute("SELECT id FROM users WHERE name = ?", request.form.get("receiver_name"))[0]["id"]
            rows5 = db.session.execute("SELECT * FROM rec WHERE product_id = ? AND user_id = ?", product, receiver)

            if len(rows5) == 1:
                flash("This Item Has Already Been Reccomended To Your Friend")
                return render_template("rec.html")

            sender = db.session.execute("SELECT id FROM users WHERE name = ?", request.form.get("sender_name"))[0]["id"]

            if sender != session["user_id"]:
                flash("You Can Only Send Reccomendations Under Your Name")
                return render_template("rec.html")

            else:
                sender = db.session.execute("SELECT id FROM users WHERE name = ?", request.form.get("sender_name"))[0]["id"]
                receiver = db.session.execute("SELECT id FROM users WHERE name = ?", request.form.get("receiver_name"))[0]["id"]
                restaurant = db.session.execute("SELECT id FROM restaurants WHERE name = ?", request.form.get("restaurant"))[0]["id"]
                product = db.session.execute("SELECT id FROM product WHERE name = ?", request.form.get("item"))[0]["id"]

                db.session.execute("INSERT INTO rec (user_id, restaurant_id, product_id, sender_id) VALUES(?, ?, ?, ?)", receiver, restaurant, product, sender)


                flash("Reccomendation Sent!")
                return render_template("rec.html")

        if request.form.get("addcartbutton"):

            if not request.form.get("quantity"):
                flash("Must Provide a Quantity")
                return redirect("/rec")

            restaurantname = request.form.get("restaurantname")
            restaurant_dict = db.session.execute("SELECT id FROM restaurants WHERE name = ?", restaurantname)
            restaurant = restaurant_dict[0]["id"]

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            quantitydict = request.form.get("quantity")
            quantity = int(quantitydict)

            db.session.execute("INSERT INTO cart (user_id, restaurant_id, product_id, quantity) VALUES (?, ?, ?, ?)", session["user_id"], restaurant, product, quantity)

            flash("Item Added to Cart!")
            return redirect("/rec")

        elif request.form.get("removebutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            db.session.execute("DELETE FROM rec WHERE product_id = ? AND user_id = ?", product, session["user_id"])

            flash("Item Removed From Reccomendations!")
            return redirect("/rec")


@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():

    if request.method == "GET":

        carts = db.session.execute("SELECT * FROM cart WHERE user_id = ?", session["user_id"])
        total = 0.00

        for cart in carts:
            restaurant = cart["restaurant_id"]
            product = cart["product_id"]
            quantity = cart["quantity"]


            cartres = db.session.execute("SELECT name FROM restaurants WHERE id = ?", restaurant)
            cartprod = db.session.execute("SELECT name FROM product WHERE id = ?", product)
            price = db.session.execute("SELECT price FROM product WHERE id = ?", product)

            cart["cartres"] = cartres[0]["name"]
            cart["cartprod"] = cartprod[0]["name"]
            cart["price"] = price[0]["price"] * quantity

            total = round(total + cart["price"], 2)

        return render_template("cart.html", carts = carts, total = total)

    if request.method == "POST":

        if request.form.get("removebutton"):

            productname = request.form.get("productname")
            productdict = db.session.execute("SELECT id FROM product WHERE name = ?", productname )
            product = productdict[0]["id"]

            db.session.execute("DELETE FROM cart WHERE product_id = ?", product)

            flash("Item Removed From Your Cart!")
            return redirect("/cart")

        elif request.form.get("purchasebutton"):

            db.session.execute("INSERT INTO orders (user_id, restaurant_id, product_id, quantity) SELECT user_id, restaurant_id, product_id, quantity FROM cart WHERE user_id = ?", session["user_id"])
            db.session.execute("DELETE FROM cart")

            return render_template("purchased.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

            # Ensure username was submitted
            if not request.form.get("username"):
                flash("Must Provide a Username")
                return render_template("login.html")

            # Ensure password was submitted
            elif not request.form.get("password"):
                flash("Must Provide a Password")
                return render_template("login.html")

            # Query database for username
            rows = db.session.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

            # Ensure username exists and password is correct
            if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
                flash("Inccorect Username/Password")
                return render_template("login.html")

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
    if request.method == "GET":
        flash("Password requires a number and should be at least 7 characters")
        return render_template("register.html")

    if request.method == "POST":

        #error checking

        rows = db.session.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if not request.form.get("name"):
            flash("Must Provide a Full Name")
            return render_template("register.html")

        if not request.form.get("email"):
            flash("Must Provide an Email")
            return render_template("register.html")

        if not request.form.get("username"):
            flash("Must Provide a Username")
            return render_template("register.html")

        if len(rows) == 1:
            flash("Username Already Exists")
            return render_template("register.html")

        # Ensure password was submitted
        if not request.form.get("password") or not request.form.get("confirmation"):
            flash("Must Provide a Password and Confirmation")
            return render_template("register.html")

        elif re.search('[0-9]', request.form.get("password")) is None:
            flash("Password Must Include a Number")
            return render_template("register.html")

        elif len(request.form.get("password")) < 7:
            flash("Make sure your password is at least 7 characters")
            return render_template("register.html")

        if not request.form.get("password") == request.form.get("confirmation"):
            flash("Passwords Do Not Match")
            return render_template("register.html")

        else:
            name = request.form.get("name")
            email = request.form.get("email")
            username = request.form.get("username")
            password = request.form.get("password")
            hash = generate_password_hash(password)
            db.session.execute("INSERT INTO users (name, email, username, hash) VALUES(?, ?, ?, ?)", name, email, username, hash)

            return render_template("login.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    flash("Handle Error")


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)