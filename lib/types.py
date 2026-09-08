"""
Contains all unique types used accross this program
"""
from enum import Enum, unique


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

    def price(self):
        return self.price


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
        }

class Catagory:
    def __init__(self, title, image="", contents=[]):
        self.title = title;
        self.contents = contents;
        self.image = image;

    def todict(self):
        return {
            "radio": 1,
            "title": self.title,
            "safe_name": self.title.replace(" ", "_").lower(),
            "image": self.image,
            "contents": [product.todict() for product in self.contents],
            "price": sum([product.price for product in self.contents]) / len(self.contents)
        }
