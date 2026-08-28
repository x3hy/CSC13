"""
Main program code
"""

import flask


def main(SCALE: float, PORT: int) -> int:
    app = flask.Flask(__name__)
    app.run(port = PORT)
    return e.EXIT_SUCCESS.value
