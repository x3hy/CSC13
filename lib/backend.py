from flask import Flask, render_template
from lib.types import exitcodes as e
from os.path import abspath

# Backend stuff
def init_backend(PORT:int) -> int:
    template_dir = abspath("./con/")
    static_dir = abspath("./con/src")

    app = Flask(__name__, template_folder = template_dir, static_folder = static_dir)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # Homepage magic
    @app.route("/")
    def homepage():
        return render_template("index.html", PRODUCTS = [
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
                {
                    "title": "Product name",
                    "image": "img/python.png",
                    "price": 123,
                    "maxamount": 123,
                    "description": "blah blah blah",
                    "id": 0
                },
            ])

    app.run(port=PORT)
    return e.EXIT_SUCCESS.value
