"""
Main program code
"""

from time import sleep
from lib.types import exitcodes as e

from multiprocessing import Process as process
from lib.frontend import init_frontend
from lib.backend import init_backend

# Manages frontend-backend lifetime sync (frontend priority)
def main(PORT: int, ISOLATEBACKEND:bool, ISOLATEFRONTEND:bool) -> int:
    if (ISOLATEBACKEND):
        print("Only running backend")
        init_backend(PORT)

    if (ISOLATEFRONTEND):
        print("Only running frontend")
        init_frontend(PORT)

    if not (ISOLATEFRONTEND) and not (ISOLATEBACKEND):
        print("Running application")
        frontend = process(target=init_frontend, args=(PORT,))
        backend  = process(target=init_backend, args=(PORT,))

        backend.start();
        sleep(0.5)
        frontend.start()

        frontend.join();
        backend.terminate();
        backend.join();

    print("Application closing..")
    return e.EXIT_SUCCESS.value
