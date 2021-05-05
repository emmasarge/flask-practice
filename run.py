import os
import json
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<products_name>")
def about_products(products_name):
    products = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == products_name:
                products = obj
    return render_template("products.html", products=products)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)