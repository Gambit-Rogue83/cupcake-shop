from flask import Flask, render_template, url_for, redirect
import csv
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    images = []
    with open("cupcakes.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            images.append({"image": row["image"], "name": row["name"], "price": row["price"]})
    return render_template("menu.html", images=images)

@app.route("/cart")
def cart():
    cupcakes=get_cupcakes("orders.csv")

    cupcakes_counted = []
    cupcake_set = set()

    for cupcake in cupcakes:
        cupcake_set.add((cupcake["name"], cupcake["price"], cupcakes.count(cupcake)))


    return render_template("cart.html", cupcakes=cupcake_set)

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake=cupcake)
        return redirect(url_for("menu"))
    else:
        return "Sorry cupcake not found."


if __name__ == "__main__":
    app.run(debug=True, port = 8000, host = "localhost")


 # previously in menu endpoint
 # images = ["cherry.jpg", "caramel-swirl.jpg", "lemon.jpg", "mint.PNG", "coconut.jpg", "hazel.jpg", "berry.jpg", "crunch.jpg"]
