from cgitb import text
from random import choice
from textwrap import fill
from tkinter import *
import pandas

ANSWER_LANG = "English"
QUIZ_LANG = "Korean"

# --- new word ---


def get_words():
    try:
        letter_frame = pandas.read_csv("words_to_learn.csv")
    except FileNotFoundError:
        letter_frame = pandas.read_csv("letter/en-ko.csv")

    words = [{"en": row.en, "ko": row.ko} for i, row in letter_frame.iterrows()]
    return words


words = get_words()

# --- game ---

timer = None
word = {}


def next_card():
    global timer, word

    if timer:
        window.after_cancel(timer)

    word = choice(words)
    canvas.itemconfig(image_id, image=front_card_img)
    canvas.itemconfig(lang_id, text=ANSWER_LANG, fill="black")
    canvas.itemconfig(word_id, text=word["en"], fill="black")

    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(image_id, image=back_card_img)
    canvas.itemconfig(lang_id, text=QUIZ_LANG, fill="white")
    canvas.itemconfig(word_id, text=word["ko"], fill="white")


# --- btn handler ---


def change_word(id, word):
    canvas.itemconfig(id, text=word)


def handle_check():
    words.remove(word)

    pandas.DataFrame(words).to_csv("words_to_learn.csv")
    next_card()


def handle_wrong():
    next_card()


# --- tkinter ui ---

GREEN = "#aaeabc"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

window = Tk()
window.config(padx=50, pady=50, background=GREEN)


canvas = Canvas(width=800, height=526, background=GREEN, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
image_id = canvas.create_image(400, 263, image=front_card_img)

lang_id = canvas.create_text(400, 150, font=LANG_FONT, text=ANSWER_LANG)
word_id = canvas.create_text(400, 263, font=WORD_FONT)
next_card()


x_image = PhotoImage(file="images/wrong.png")
x_btn = Button(image=x_image, highlightthickness=0, bd=0, command=handle_wrong)
x_btn.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_btn = Button(image=check_image, highlightthickness=0, bd=0, command=handle_check)
check_btn.grid(row=1, column=1)

window.mainloop()
