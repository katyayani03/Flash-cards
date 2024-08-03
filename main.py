from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#you can create your own csv file of any subject you want to make flash cards of
#the csv file should have 2 columns, the first one questions and the second one answers
try:
    data_frame = pandas.read_csv("data/words to learn.csv")
except FileNotFoundError:
    og_data_frame = pandas.read_csv("data/french_words.csv")
    cards = og_data_frame.to_dict(orient="records")  # list of dictionaries[{"French": , "English":}
else:
    cards = data_frame.to_dict(orient="records") # list of dictionaries[{"French": , "English":}
current_card = {}

#remove the card you have learned
def remove_card():
    cards.remove(current_card)
    data = pandas.DataFrame(cards)
    data.to_csv("data/words to learn.csv", index=False)
    change_card()

def flash_card():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white") #you can replace the "English" here with the Question part of your dataframe


def change_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(cards) #start with any card
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black") #you can replace the "French" here with the Question part of your dataframe
    flip_timer = window.after(3000, flash_card)


# ---------------------------------------------------UI---------------------------------------------------#
window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flash_card)

canvas = Canvas(window, width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=change_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

change_card()

window.mainloop()
