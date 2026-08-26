"""
Contains all unique types used accross this program
"""
from enum import Enum, unique

@unique
class exitcodes(Enum):
    EXIT_SUCCESS = 0
    EXIT_FALIURE = 1
    ARG_NOT_FOUND = 2


class Theme:
    background = "#ff0000"
    foreground = "#00ff00"
