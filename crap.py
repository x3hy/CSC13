#2c

# Define a class called Class
class Class:
    def __init__(self, student_list):
        self.student_list = student_list

    def list(self):
        return self.student_list

    def new(self, student):
        self.student_list.append(student)

    def rem(self, student):
        self.student_list.remove(student)

# Create a class of students
B6 = Class(["John Smith", "Johnier Smith", "John Doe", "John Deer"]);
print( B6.list() )

# Add a new student
B6.new("Cool Person");
print( B6.list() )

# Remove a student
B6.rem("John Smith")
print( B6.list() )


exit()

#2a
import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="Comp Sci Diva")
label.pack()
root.mainloop()

# 2b
import os
fname = "test123.txt"

"""
Set bitwise flags for:
 - Creating file if not existing
 - Open file in read and write mode
"""
flags = os.O_CREAT | os.O_RDWR

"""
Get a pointer to the file descriptor
with read/write groups.
"""
fd = os.open(fname, flags, 0o644);

# Open the file descriptor and write to it
os.write(fd, b"Hellllooo file!")

"""
Write repositions the pointer to the
end of the written memory, we can
reset the progress by simply seeking
back to the start of the file pointer.
"""
os.lseek(fd, 0, os.SEEK_SET)

# Print the written content
with os.fdopen(fd, "r") as f:
    content = f.read()
    print(content)

