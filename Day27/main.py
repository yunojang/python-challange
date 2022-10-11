from tkinter import *

window = Tk()
window.title("First python(tkinter) GUI Program")
window.minsize(width=500, height=300)


# Label
first_label = Label(text="I'm a Label", font=("Arial", 24))
# first_label.pack(side="left")
first_label.pack()


def button_clicked():
    input_text = input.get()
    new_text = input_text if input_text else "Clicked!!"
    input.insert(END, string="'insert'")
    first_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

input = Entry()
input.pack()
input.config(width=10)


text_box = Text(height=5)
text_box.pack()

spin = Spinbox()
spin.pack()

slider = Scale()
slider.pack()


def check_used():
    print(check_state.get())


check_state = IntVar()
check = Checkbutton(text="is on", variable=check_state, command=check_used)
print(check_state)

check.pack()
