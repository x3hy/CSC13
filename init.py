from lib.arg import args
from lib.types import exitcodes as e
from lib.main import main
from sys import argv
import socket


# Set up command line arguments
arg:object = args (argv, "MyApp");
arg.addcheck ("--port", "Set the port for the backend");
arg.addcheck ("--frontend-only", "ONLY run the frontend");
arg.addcheck ("--backend-only", "ONLY run the backend");
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
APP_PORT: int = 6769;
if (arg.hasv ("--port")):
    APP_PORT = int(arg.getv("--port"));

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    if (s.connect_ex(("localhost", APP_PORT)) == 0):
        print(f"Port {APP_PORT} already in use..")
        arg.help()
        exit (e.EXIT_FALIURE.value)

FRONTEND: bool = False
if (arg.hasv ("--frontend-only")):
    FRONTEND = True

BACKEND: bool = False
if (arg.hasv ("--backend-only")):
    BACKEND = True


# Run the main app
if __name__ == "__main__":
    rc: int = main (APP_PORT, BACKEND, FRONTEND);
    exit (rc);
