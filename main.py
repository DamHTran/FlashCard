from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CREATE FLASH CARD ------------------------------- #
df = pandas.read_csv("data/finnish_words.csv")
word_list = df.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    finnish_word = current_card["Finnish"]
    canvas.itemconfig(card_title, text="Finnish", fill="black")
    canvas.itemconfig(card_word, text=finnish_word, fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_img)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(408, 250, image=front_img)
back_img = PhotoImage(file="images/card_back.png")
card_title = canvas.create_text(400, 150, text="", fill= "black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


unknown_image = PhotoImage(file="images/wrong.png")
button = Button(image=unknown_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
button.grid(column=0, row=1)


check_image = PhotoImage(file="images/right.png")
button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
button.grid(column=1, row=1)

next_card()









window.mainloop()

