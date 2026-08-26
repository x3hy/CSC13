import lib.arg as arg
from sys import argv


# Set up command line
arg = arg.args(argv, "MyApp")
arg.addcheck("-dpi", "Set scale of the program")


# Catch invalid command line arguments
if len(arg.check()):
    arg.help()

    print()
    for a in arg.check():
        print("Option not found: " + a)

    exit()


# Print --test value if provided
APP_SCALE = 1
if (arg.hasv("-dpi")):
    APP_SCALE = int(arg.getv("-dpi"))


print(APP_SCALE)
