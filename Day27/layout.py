from tkinter import *

screen = Tk()
screen.minsize(width=300, height=200)
screen.title("layout")

my_label = Label(text="Hello")
my_label.grid(column=0, row=0)

button = Button(text="Click me")
button.grid(column=1, row=1)

input_box = Entry()
input_box.grid(column=3, row=2)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

screen.mainloop()
