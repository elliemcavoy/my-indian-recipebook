import os
import random
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_split import split
from flask_paginate import Pagination, get_page_parameter
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from collections import Counter
from pymongo import MongoClient
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

PER_PAGE = 6


# Homepage
# Geeks for geeks used to implement the Counter functionality
@app.route("/")
@app.route("/index")
def index():
    """
    Pulls the top three most upvoted recipes and parses them into leaderboard.
    The index.html page is rendered with these details.
    """
    x = []
    results = mongo.db.vote.find({"vote": "upvote"})
    for item in results:
        recipe_name = item.get('recipe_name')
        x.append(recipe_name)
        counter1 = Counter(x)
        votes = dict(counter1.most_common(3))

    return render_template("index.html", results=results, votes=votes)


# Register for an account
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Username provided is checked against exising users, if not already in use
    user is able to provide a password and gain access to additional
    functionality.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # inserts blank array ready for favourites to be added
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourites": []
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Thank You for Registering")

    return render_template("register.html")


# Log In Function
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Function checks inputted username against exisiting username
    in users collection. If username & password match a user,
    the user will be logged in.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                                    existing_user["password"],
                                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                            "my_profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Log Out
@app.route("/logout")
def logout():
    """
    Deletes the session cookie to log the user out
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Will gather all information from form and enter it into a
    new document in the recipes collection
    """
    if request.method == "POST":
        image = request.form.get("image")
        # if no image provided stock image inserted
        if len(image) == 0:
            image = ("/static/images/knife&fork.jpg")
        recipe = {
            "meal_type_name": request.form.get("meal_type_name"),
            "name": request.form.get("name"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "image": image,
            "time": request.form.get("time"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added")
    meal_type = mongo.db.meal_type.find().sort("meal_type_name")
    return render_template("add_recipe.html", meal_type=meal_type)


# My Profile
@app.route("/my_profile/<username>", methods=["GET", "POST"])
def my_profile(username):
    """
    Use the session cookie to find the user & the recipes
    they have added & their favourites.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        my_recipes = mongo.db.recipes.find({"created_by": session["user"]})
        user = mongo.db.users.find_one({"username": session["user"]})
        recipes = mongo.db.recipes.find()

        return render_template("my_profile.html", username=username,
                               my_recipes=my_recipes,
                               recipes=recipes, user=user)


# All Recipes
# pagination implemented with help from:
# https://stackoverflow.com/questions/54053873/implementation-of-pagination-using-flask-paginate-pymongo
@app.route("/recipes")
def recipes():
    """
    All recipes from recipes collection displayed
    with 6 recipes per page.
    """
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    allrecipe = mongo.db.recipes.find().skip(
                                            (page - 1) * PER_PAGE).limit(
                                            PER_PAGE)
    pagination = Pagination(page=page, per_page=6, total=allrecipe.count(),
                            search=search, record_name='allpost')
    return render_template('recipes.html', recipes=allrecipe,
                           pagination=pagination)


# Recipes Search
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Will search for the keyword(s) provided and return
    any results.
    """
    query = request.form.get("query")
    recipe_results = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    results = list(recipe_results)
    if len(results) == 0:
        flash("No recipes found")
    return render_template("recipes.html", recipes=recipe_results)


# Recipecard
@app.route("/recipecard/<recipe>")
def recipecard(recipe):
    """
    Will find the recipe by its ObjectId and
    return the details of the selected recipe.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe)})
    method = recipe.get("method").split(".")
    ingredients = recipe.get("ingredients").split(",")
    time = recipe.get("time")
    return render_template("recipecard.html", recipe=recipe,
                           method=method, ingredients=ingredients,
                           time=time)


# Add to favourites
# assistance from Tutor Support was required to implement this functionality
@app.route("/add_favourites/<recipe>", methods=["GET", "POST"])
def add_favourites(recipe):
    """
    Add recipe to favourites field in the users
    collection.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe)})
    recipe_id = recipe.get("_id")
    if request.method == "POST":
        mongo.db.users.find_one_and_update(
            {"username": session["user"]},
            {"$addToSet": {"favourites": recipe_id}}
        )
        flash("Recipe Added to Favourites")

    recipe = recipe.get("_id")
    return recipecard(recipe)


# Remove Favourite
@app.route("/remove_favourite/<recipe>", methods=["GET", "POST"])
def remove_favourite(recipe):
    """
    Finds recipe ID in the users collection and removes.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe)})
    recipe_id = recipe.get("_id")
    mongo.db.users.find_one_and_update(
        {"username": session["user"]},
        {"$pull": {"favourites": recipe_id}}
    )
    flash("Recipe removed from Favourites")
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return my_profile(username)


# Delete Recipe
@app.route("/delete_recipe/<recipe>")
def delete_recipe(recipe):
    """
    Removes recipe details from the recipes collection.
    """
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe)})
    flash("Recipe Successfully Deleted")
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return my_profile(username)


# Edit Recipe
@app.route("/edit_recipe/<recipe>", methods=["GET", "POST"])
def edit_recipe(recipe):
    """
    Updates the details of the specified recipe.
    """
    meal_type = mongo.db.meal_type.find().sort("meal_type_name")
    if request.method == "POST":
        image = request.form.get("image")
        if len(image) == 0:
            image = ("/static/images/knife&fork.jpg")
        submit = {
            "meal_type_name": request.form.get("meal_type_name"),
            "name": request.form.get("name"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "time": request.form.get("time"),
            "image": image,
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe)}, submit)
        flash("Recipe Updated")
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe)})
    return render_template("edit_recipe.html", recipe=recipe,
                           meal_type=meal_type)


# Voting
@app.route("/voting/<recipe>", methods=["GET", "POST"])
def voting(recipe):
    """
    Inserts the recipe name & the vote (either up or down)
    into votes collection.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe)})
    name = recipe.get("name")
    if request.method == "POST":
        votes = {
            "vote": request.form.getlist('vote'),
            "recipe_name": name,
            "added_by": session["user"]
        }
        mongo.db.vote.insert_one(votes)
        flash("Thank you for voting")
    recipe = recipe.get("_id")
    return recipecard(recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
