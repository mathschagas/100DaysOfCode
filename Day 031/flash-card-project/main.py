from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    words_df = pandas.read_csv("Day 031/flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Day 031/flash-card-project/data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words_df.to_dict(orient="records")


# ---------------------------- PICK RANDOM CARD ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Português", fill="white")
    canvas.itemconfig(card_word, text=current_card["Portugues"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Day 031/flash-card-project/data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- # 

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_back_image = PhotoImage(file="Day 031/flash-card-project/images/card_back.png")
card_front_image = PhotoImage(file="Day 031/flash-card-project/images/card_front.png")
right_image = PhotoImage(file="Day 031/flash-card-project/images/right.png")
wrong_image = PhotoImage(file="Day 031/flash-card-project/images/wrong.png")

canvas = Canvas(height=526, width=800)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()