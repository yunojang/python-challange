from cgitb import text
from msilib.schema import File
from tkinter import *
from turtle import title

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TITLE_FONT = ("Arial", 18, "bold")
TIME_FONT = (FONT_NAME, 30, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Pomodoro", fg=RED)
    check_label.config(text="")
    canvas.itemconfig(timer_id, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps > 8:
        return

    if reps == 8:
        count_down_timer(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=GREEN)
    elif reps % 2 != 0:
        count_down_timer(WORK_MIN * 60)
        title_label.config(text="Work", fg=RED)
    elif reps % 2 == 0:
        count_down_timer(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM  ------------------------------- #


def get_time_text(count):
    # hour = int(count / 60)
    # hour_text = str(hour) if len(str(hour)) > 1 else "0" + str(hour)
    hour_text = str(int(count / 60)).zfill(2)

    # sec = count % 60
    # sec_text = str(sec) if len(str(sec)) > 1 else "0" + str(sec)
    sec_text = str(count % 60).zfill(2)

    return f"{hour_text}:{sec_text}"


def count_down_timer(count):
    global reps

    canvas.itemconfig(timer_id, text=get_time_text(count))
    if count > 0:
        global timer
        timer = window.after(1, count_down_timer, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(reps / 2)

        for _ in range(work_sessions):
            marks += "✔"
            check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg=YELLOW, padx=30, pady=20)

title_label = Label(text="Pomodoro", bg=YELLOW, fg=RED, font=TITLE_FONT)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
canvas.grid(row=1, column=1)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

timer_id = canvas.create_text(100, 132, text="00:00", fill="white", font=TIME_FONT)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(bg=YELLOW, text="", fg=GREEN, font=TITLE_FONT)
check_label.grid(row=3, column=1)

window.mainloop()
