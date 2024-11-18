from tkinter import *
import random

attempts = 10

answer = random.randint(1,99)

def check_answer():
    global attempts
    global text

    attempts -= 1
    
    guess = int(entry_window.get())

    if answer == guess:
        text.set("Congradulations! YOU WON!")
        btn_check.pack_forget()

    elif attempts == 0:
        text.set("You ran out of attempts! Try again next time!")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect! You have " + str(attempts) + "remaining - Go a bit higher!")
    elif guess > answer:
        text.set("Incorrect! You have " + str(attempts) + "remaining - Go a bit lower!")

    
    return

root=Tk()

root.title("Guess that Number#")

root.geometry('500x158')

Label = Label(root, text="Guess the number between 1 through 100")
Label.pack()

entry_window = Entry(root,width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Check", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Quit", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 10 attempts remaining! Good luck!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()  