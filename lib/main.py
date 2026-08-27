"""
Main program code
"""
from lib.types import exitcodes as e
from lib.types import *
import customtkinter as ctk
from PIL import Image

# Custom components
class cui(ctk.CTk):
    def __init__(self, name, width, height):
        super().__init__();
        self.title(name);
        self.geometry(f"{width}x{height}");
        self.current_width = width;
        self.current_height = height;

        # bind the resize event to the on_resize function
        self.bind("<Configure>", self.on_resize)


    # Run on resize event
    def on_resize(self, event):
        if event.widget == self:
            if event.width != self.current_width:
                self.current_width = event.width;

            if (event.height != self.current_height):
                self.current_height = event.height;

            print(f"{self.current_width}x{self.current_height}");


    # Draw rectangle
    def rect(self, x, y, w, h, color):
        if type(w) == float:
            w = self.current_width * w;

        if type(h) == float:
            h = self.current_height * h;

        out = ctk.CTkFrame(self, width=w, height=h, fg_color = color, corner_radius=0);
        out.place(x = x, y = y);
        return out;


def main(SCALE: float) -> int:
    if (SCALE != 0):
        # Change scaling
        ctk.deactivate_automatic_dpi_awareness()
        ctk.set_window_scaling(SCALE)
        ctk.set_widget_scaling(SCALE)

    # Initialise the app
    app = cui("test123", 400, 300);
    app.rect(0,0,0.5,1.0, "#ff0000");

    app.mainloop()
    return e.EXIT_SUCCESS.value
