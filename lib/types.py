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
    def __init__(self, title, desc, price, maxamount, image):
        self.title = title
        self.desc = desc
        self.price = price
        self.maxamount = maxamount
        self.image = image

    # Return the item as a dict
    def dict(self):
        return {
            "title": self.title,
            "desc": self.desc,

            # For compatability
            "description": self.desc,
            "price": self.price,
            "maxamount": self.maxamount,
            "image": str(self.image)
        }