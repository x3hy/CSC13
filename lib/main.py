"""
Main program code
"""
from lib.types import exitcodes as e
import tkinter as tk

def main(SCALE: float) -> int:
    root = tk.Tk()
    root.configure(bg="#0000ff")
    root.title("test123")
    root.geometry("400x300")
    root.attributes("-topmost", True)
    root.tk.call("tk", "scaling", SCALE)
    label = tk.Label(root, text="Hello World", bg="black", fg="white")
    button = tk.Button(root, text="Click Me", bg="#ff0000", fg="#ffffff", relief="groove")

    label.pack()
    button.pack()

    root.mainloop()
    return e.EXIT_SUCCESS.value
