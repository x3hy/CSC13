"""
Main program code
"""
from lib.types import exitcodes as e
from lib.types import *
import customtkinter as ctk


# Custom components
class cui:
    def __init__(self, title, geom):
        self.app = ctk.CTk();
        self.app.title(title);
        self.app.geometry(geom);

        # Change BACKGROUND color (weird method)
        self.app.configure(fg_color=Theme.background)
        self.app.update_idletasks()

    def button(self, text = None, command = None, padx = 0, pady = 0):
        rbutton = ctk.CTkButton(master=self.app, text=text, command=command);
        rbutton.pack(padx=padx, pady=pady);
        return rbutton

    def run(self):
        return self.app.mainloop()

    def app(self):
        return self.app

def main(SCALE: float) -> int:
    if (SCALE != 0):
        # Change scaling
        ctk.deactivate_automatic_dpi_awareness()
        ctk.set_window_scaling(SCALE)
        ctk.set_widget_scaling(SCALE)

    # Initialise the app
    app = cui("test123", "400x300");

    #label = ctk.CTkLabel(master=app, text="Welcome to CustomTkinter", font=("Arial", 20))
    #label.pack(padx=20, pady=20)

    button = app.button("test123");
    print(f"{app.app.winfo_width()}")
    app.run ()

    return e.EXIT_SUCCESS.value
