from flask import Flask, render_template
from lib.types import exitcodes as e
from lib.types import Product
from logging import getLogger, ERROR
from os.path import abspath
import click

PRODUCTS = [
    Product("Walls", "Sturdy non-american walls.", 12.5, -1, "img/python.png"),
    Product("Carpet", "Awesome rug-like-carpet", 1, -1, "img/python.png"),
    Product("Lamps", "Gay lamps", 148723.23, -1, "img/python.png"),
    Product("Rug", "Cool carpet-like-rug", 8.008, -1, "img/python.png")
]

PRODUCTS_DICT = [product.dict() for product in PRODUCTS];

# Backend stuff
def init_backend(PORT:int) -> int:
    template_dir = abspath("./con/")
    static_dir = abspath("./con/src")
    app = Flask(__name__, template_folder = template_dir, static_folder = static_dir)

    # Disable caching of templates
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # Disable flask output
    log = getLogger("werkzeug");
    log .setLevel(ERROR);
    def secho(text, file=None, nl=None, err=None, color=None, **styles):
        pass

    def echo(text, file=None, nl=None, err=None, color=None, **styles):
        pass

    # Redirect logging to blank functions (disabling initial output)
    click.echo = echo
    click.secho = secho


    # Homepage magic
    @app.route("/")
    def homepage():
        print("Connection to /");
        products = [];
        return render_template("index.html", PRODUCTS = PRODUCTS_DICT)

    print("Started backend server");
    app.run(port=PORT)
    return e.EXIT_SUCCESS.value
