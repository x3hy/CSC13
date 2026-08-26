from lib.arg import args
from lib.types import exitcodes as e
from lib.main import main
from sys import argv


# Set up command line arguments
arg:object = args (argv, "MyApp");
arg.addcheck ("-dpi", "Set scale of the program");
arg.addcheck ("-h", "Show this menu");


# Catch invalid command line arguments
if len (arg.check()):
    arg.help ();

    print ();
    for a in arg.check():
        print ("Option not found: " + a);

    exit (e.ARG_NOT_FOUND.value);


# Behavior for the -h flag
if (arg.hasv ("-h")):
    arg.help ();
    exit (e.EXIT_SUCCESS.value);


# Handle -dpi and APP_SCALE variable
APP_SCALE: float = 0.0;
if (arg.hasv ("-dpi")):
    APP_SCALE = float (arg.getv("-dpi"));


# Run the main app
if __name__ == "__main__":
    rc: int = main (APP_SCALE);
    exit (rc);
