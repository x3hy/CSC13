"""
Main program code
"""
from lib.types import exitcodes as e
from lib.types import *
import customtkinter as ctk


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
        self.grid_rowconfigure(0, weight=1);
        self.grid_columnconfigure(0, weight=1);



    def grid_frame(self, master, row = 0, column = 0, rows = None, columns = None, bg = Theme.background, align="nesw"):
        out = ctk.CTkFrame(master = master, fg_color=bg, corner_radius=0);


        # Place the frame onto the app grid
        out.grid(row = row, column = column, sticky=align);
        out.grid_propagate(False)


        # Create rows
        if rows is not None:
            for index, weight in enumerate(rows):
                out.grid_rowconfigure(index, weight=weight);

        # Create columns
        if columns is not None:
            for index, weight in enumerate(columns):
                out.grid_columnconfigure(index, weight=weight);

        return out


    # Run on resize event
    def on_resize(self, event):
        if event.widget == self:
            if event.width != self.current_width:
                self.current_width = event.width;

            if (event.height != self.current_height):
                self.current_height = event.height;

            print(f"{self.current_width}x{self.current_height}");


def main(SCALE: float) -> int:
    if (SCALE != 0):
        # Change scaling
        ctk.deactivate_automatic_dpi_awareness()
        ctk.set_window_scaling(SCALE)
        ctk.set_widget_scaling(SCALE)

    # Initialise the app
    app = cui("test123", 400, 300);

    # Make main frame
    body = app.frame(app, 0, 0, [1], [0,1], bg="#ff0000")

    # Sub-sections
    left_panel = grid.frame(body, 0, 0, [1], [1], bg="#00ff00")
    rest = app.frame(body, 0, 1, bg="#0000ff")

    btn1 = ctk.CTkButton(left_panel, text="Sub [0,0]", corner_radius=0)
    btn1.grid(row=0, column=0, sticky="nwe", padx= 0, pady = 0)
    btn2 = ctk.CTkButton(left_panel, text="Sub [0,0]", corner_radius=0)
    btn2.grid(row=1, column=0, sticky="nwe", padx= 0, pady = 0)

    app.mainloop()
    return e.EXIT_SUCCESS.value
