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


class Theme:
    background = "#ffffff"
    foreground = "#000000"
    surface = "#999999"
    opad = 5
    ipad = 5
