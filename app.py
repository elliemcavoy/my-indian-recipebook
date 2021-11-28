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
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        
        session["user"] = request.form.get("username").lower()
        flash("Thank You for Registering")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
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


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    
    if request.method == "POST":
        recipe = {
            "meal_type_name": request.form.get("meal_type_name"),
            "name": request.form.get("name"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added")
        
    meal_type = mongo.db.meal_type.find().sort("meal_type_name")
    return render_template("add_recipe.html", meal_type=meal_type)
    
@app.route("/my_profile/<username>", methods=["GET", "POST"])
def my_profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        my_recipes=mongo.db.recipes.find({"created_by": session["user"]})
        return render_template("my_profile.html", username=username, my_recipes=my_recipes)

    return redirect(url_for("login"))


@app.route("/recipes")
def recipes():
    recipes=mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipecard/<recipe>", methods=["GET", "POST"])
def recipecard(recipe):
    recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe)})

    return render_template("recipecard.html", recipe=recipe)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = mongo.db.recipes.find({"$text": {"$search": query}})
    return render_template("recipes.html", recipes=recipes)

#@app.route("/add_favourites/<recipe>", methods=["GET", "POST"])
#def add_favourites(recipe):
    #if request.method == "POST":
        #recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe)})
        #favourite={
            #"meal_type_name": "{{recipe.meal_type}}",
            #"name": "{{recipe.name}}",
            #"ingredients": "{{recipe.ingredients}}",
            #"method": "{{recipe.method}}",
            #"added_by": session["user"]
        #}
        #mongo.db.favourites.insert_one(favourite)
        #flash("Recipe Added to Favourite")
    

@app.route("/delete_recipe/<recipe>")
def delete_recipe(recipe):
    mongo.db.recipes.remove({"_id": ObjectId(recipe)})
    flash("Recipe Successfully Deleted")
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    my_recipes=mongo.db.recipes.find({"created_by": session["user"]})
    return render_template("my_profile.html", username=username, my_recipes=my_recipes)


    



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

