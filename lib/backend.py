from flask import Flask, render_template, request
from lib.types import Product, Catagory
from logging import getLogger, ERROR
from lib.types import exitcodes as e
from os import name as platform
from flask_cors import CORS
from os.path import abspath
import click


# Documentation in lib/types.py
PRODUCTS = [

    # Bathroom catagory:
    Product("Tiles, spa bath, shower and tapware", 2500, 10, "Bathroom upgrade pack", "img/tapware.png"),

    # Kitchen catagory radio
    Catagory("Kitchen products", "img/python.png", [
        Product("Upgrades units and worktop",      2500),
        Product("As A plus induction hob",         2500),
        Product("As A plus Deluxe appliance pack", 2500)
    ]),

    # Living room TV options
    Catagory("TV Point", "img/python.png", [
        Product("With roof-mounted aerial", 250),
        Product("Withsatellite dish",      250)
    ]),

    # Living room heat pump options
    Catagory("Heat Pump", "img/python.png", [
        Product("4.5KW", 2500),
        Product("2.5KW", 1800)
    ]),

    # Misc network/electrical upgrades
    Product("Additional 1G electrical sockets", 40, -1, " Electrical Sockets", "img/python.png"),
    Product("Up to 8 additional network points (already comes with 2)", 50, 8, "Network points", "img/python.png")
]

PRODUCTS_DICT = [product.todict() for product in PRODUCTS];
ORDERS_DICT = []

# Backend stuff
def init_backend(PORT:int) -> int:
    template_dir = abspath("./pagedata/")
    static_dir = abspath(f"{template_dir}/src")

    # Check if platform is DOS
    if (platform == "nt"):
        print("Detected DOS platform")
        template_dir = abspath("templates")
        static_dir = abspath(f"{template_dir}/src")

    print("Using templates: " + template_dir)
    print("Using static: " + static_dir)

    app = Flask(__name__, template_folder = template_dir, static_folder = static_dir)
    CORS(app);

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
        print(PRODUCTS_DICT)
        return render_template("index.html", PRODUCTS = PRODUCTS_DICT)

    @app.route("/checkout_page")
    def checkoutpage():
        print("Connection to checkout page");
        return render_template("checkout.html");

    @app.route('/checkout', methods = ['POST'])
    def checkout():
        print("checkout");

        # prints out UUIDS
        if (request.method == "POST"):
            print(request.get_json());

            for product in request.get_json():
                for item in PRODUCTS:
                    if type(item) is Catagory:
                        for nested in item.contents:
                           if nested.uuid in request.get_json():
                                print(nested.uuid);

            return "OK", 200

        else:

            # Invalid method
            return "Invalid Method", 405


    print("Started backend server");
    app.run(port=PORT)
    return e.EXIT_SUCCESS.value
