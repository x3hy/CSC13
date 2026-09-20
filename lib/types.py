"""
Contains all unique types used accross this program
"""
from enum import Enum, unique
from uuid import uuid4 as uuid


@unique
class exitcodes(Enum):
    EXIT_SUCCESS  = 0
    EXIT_FALIURE  = 1
    ARG_NOT_FOUND = 2
    PORT_IN_USE   = 3


class Product:
    def __init__(self, desc, price, maxamount=-1, title="", image=""):
        self.title = title
        self.desc = desc
        self.price = price
        self.maxamount = maxamount
        self.image = image
        self.uuid = uuid().hex
        self.quantity = 0;

    def price(self):
        return self.price

    def uuid(self):
        return self.uuid

    def set_quantity(self, n: int):
        self.quantity = n;

    def get_quantity(self):
        return self.quantity


    # Return the item as a dict
    def todict(self):
        return {
            "title": self.title,
            "desc": self.desc,
            "safe_name": self.desc.replace(" ", "_").lower(),

            # For compatability
            "description": self.desc,
            "price": self.price,
            "max": self.maxamount,
            "image": self.image,
            "uuid" : self.uuid
        }

class Catagory:
    def __init__(self, title, image="", contents=[]):
        self.title = title;
        self.contents = contents;
        self.image = image;
        self.uuid = uuid().hex

    def contents(self):
        return self.contents

    def uuid(self):
        return self.uuid

    def todict(self):
        return {
            "radio": 1,
            "title": self.title,
            "safe_name": self.title.replace(" ", "_").lower(),
            "image": self.image,
            "contents": [product.todict() for product in self.contents],
            "price": sum([product.price for product in self.contents]) / len(self.contents),
            "uuid": self.uuid
        }
