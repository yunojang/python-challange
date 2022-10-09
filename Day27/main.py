from tkinter import *

window = Tk()
window.title("First python(tkinter) GUI Program")
window.minsize(width=500, height=300)


# Label
first_label = Label(text="I'm a Label", font=("Arial", 24))
first_label.pack()


def button_clicked():
    text = input.get()
    first_label["text"] = text if text else "Clicked!!"


button = Button(text="Click me", command=button_clicked)
button.pack()

input = Entry()
input.pack()
input.config(width=10)

window.mainloop()
