from flask import Flask, render_template
from logging import getLogger, ERROR
from lib.types import exitcodes as e
from lib.types import Product
from os.path import abspath
from os import name as platform
import click

PRODUCTS = [
    Product("Bathroom Tiles", "Tiles for bathroom floor", 2500, -1, "img/tiles.png"),
    Product("Spa Bath", "Rich person shaped water containment device", 2500, -1, "img/spa.png"),
    Product("Bathroom Tapware", "Taps knobs and all the rest of that fun stuff..", 2500, -1, "img/tapware.png"),
    Product("TV Point A", "TV point, includes roof-mounted aerial", 250, -1, "img/aerial.png"),
    Product("TV Point B", "TV point, includes satellite dish", 250, -1, "img/radar.png"),
    Product("Heat Pump A", "4.5KW Heater", 2500, -1, "img/heatpump1.png"),
    Product("Heat Pump B", "2.5KW Heater, Max quantity: 3", 1800, 3, "img/heatpump2.png"),
    #Product(-1, "img/python.png"),
]

PRODUCTS_DICT = [product.dict() for product in PRODUCTS];

# Backend stuff
def init_backend(PORT:int) -> int:
    template_dir = abspath("./templates/")
    static_dir = abspath("./templates/src")

    if (platform == "nt"):
        template_dir = abspath("templates")
        static_dir = abspath(f"{template_dir}/src")

    print("Using templates: " + template_dir)
    print("Using static: " + static_dir)

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
