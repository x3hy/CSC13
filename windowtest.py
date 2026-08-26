import tkinter as tk

root = tk.Tk()
root.configure(bg="#0000ff")
root.title("test123")
root.geometry("400x300")
root.attributes("-topmost", True)
root.tk.call("tk", "scaling", 3.0)

label = tk.Label(root, text="Hello World", bg="black", fg="white")
button = tk.Button(root, text="Click Me", bg="#ff0000", fg="#ffffff", relief="groove")

label.pack()
button.pack()

root.mainloop()
