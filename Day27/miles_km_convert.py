from tkinter import *


def miles_to_km(mile):
    km = round(mile * 1.609, 3)
    return km


screen = Tk()
screen.config(padx=30, pady=30)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)
miles_input.insert(END, "0")

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def handle_calc():
    mile = float(miles_input.get())
    km = miles_to_km(mile)
    result_label.config(text=f"{km}")


calc_button = Button(text="Calculate", command=handle_calc)
calc_button.grid(row=2, column=1)

screen.mainloop()
