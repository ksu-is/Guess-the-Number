from tkinter import*
import random

attempts = 10
answer = random.randint(1,100)

def check_answer():
    global attmepts

    try:
       
        attempts -= 1

        guess = int(entry_window.get())

        if answer == guess:
            text.set("Congratulations! YOU WON!")
            btn_check.pack_forget()
        elif attempts == 0:
            text.set("You ran out of attempts! Try again next time!")
            btn_check.pack_forget()
        elif guess < answer:
            text.set(f"Incorrect! you have {attempts} remaining - Go a bit higher!")
        elif guess > answer:
            text.set(f"Incorrect! you have {attempts} remaining - Go a bit lower!")
    except ValueError:
        text.set("Please enter a valid mumber only (ex. 0, 1, 2, 3)")
