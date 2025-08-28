''' 
ROCK PAPPER SCISSOR'S GAME
3 variables ROCK,paper, scissor
user input and random computer input
if loop for every case :
        USER   |  COMPUTER  |OUTPUT
        R      |  R         |DRAW
        P      | P          |DRAW
        S      |S            |DRAW
    THEN SO ON
'''
# import random

# choices=["ROCK","PAPER","SCISSOR"]
# computer=random.choice(choices)
# user=input(f"ENTER YOUR CHOICE:").upper()
# print(f"USER'S CHOICE:{user}")
# print(f"COMPUTER'S CHOICE:{computer}")
# if user not in choices:
#     print("INVALID")
# else:
#     if(user==computer):
#         print("DRAW")
#     elif(user=="ROCK" and computer=="PAPER"):
#         print("USER WINS!!")
#     elif(user=="ROCK" and computer=="SCISSOR"):
#         print("USER WINS!!")
#     elif(user=="PAPER" and computer=="ROCK"):
#         print("USER WINS!!")
#     elif(user=="PAPER" and computer=="SCISSOR"):
#         print("COMPUTER WINS!!")
#     elif(user=="SCISSOR" and computer=="ROCK"):
#         print("COMPUTER WINS!!")
#     elif(user=="SCISSOR" and computer=="PAPER"):
#         print("USER WINS!!")                            
# ---------------------------------------------------------------------------------------------
# import random

# # List of choices
# choices = ["ROCK", "PAPER", "SCISSORS"]

# # Random choice for computer
# computer = random.choice(choices)

# # User input
# user = input("ENTER YOUR CHOICE (ROCK, PAPER, SCISSORS): ").upper()

# # Print choices
# print(f"USER'S CHOICE: {user}")
# print(f"COMPUTER'S CHOICE: {computer}")

# # Validate user input
# if user not in choices:
#     print("INVALID CHOICE! Please choose ROCK, PAPER, or SCISSORS.")
# else:
#     # Dictionary for win conditions
#     win_conditions = {
#         "ROCK": "SCISSORS",
#         "PAPER": "ROCK",
#         "SCISSORS": "PAPER"
#     }

#     # Determine the result
#     if user == computer:
#         print("DRAW")
#     elif win_conditions[user] == computer:
#         print("USER WINS!!")
#     else:
#         print("COMPUTER WINS!!")
# -----------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import messagebox
# import random

# # Create main window
# root = tk.Tk()
# root.title("Rock Paper Scissors Game")
# root.geometry("400x400")

# # List of choices
# choices = ["ROCK", "PAPER", "SCISSORS"]

# # Function to play game
# def play_game(user_choice):
#     computer_choice = random.choice(choices)

#     # Win conditions
#     win_conditions = {
#         "ROCK": "SCISSORS",
#         "PAPER": "ROCK",
#         "SCISSORS": "PAPER"
#     }

#     # Determine the result
#     if user_choice == computer_choice:
#         result = "DRAW"
#     elif win_conditions[user_choice] == computer_choice:
#         result = "YOU WIN!"
#     else:
#         result = "COMPUTER WINS!"

#     # Show result in a messagebox
#     messagebox.showinfo("Result", f"Computer chose: {computer_choice}\nYou chose: {user_choice}\n{result}")

# # Label for instructions
# label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
# label.pack(pady=20)

# # Buttons for user choices
# rock_button = tk.Button(root, text="ROCK", font=("Arial", 12), command=lambda: play_game("ROCK"))
# rock_button.pack(pady=5)

# paper_button = tk.Button(root, text="PAPER", font=("Arial", 12), command=lambda: play_game("PAPER"))
# paper_button.pack(pady=5)

# scissors_button = tk.Button(root, text="SCISSORS", font=("Arial", 12), command=lambda: play_game("SCISSORS"))
# scissors_button.pack(pady=5)

# # Run the application
# root.mainloop()
# ----------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import messagebox
# import random

# # Create the main window
# root = tk.Tk()
# root.title("Rock Paper Scissors")
# root.geometry("400x500")
# root.configure(bg="#222831")  # Dark background color

# # Choices list
# choices = ["ROCK", "PAPER", "SCISSORS"]

# # Dictionary for winning conditions
# win_conditions = {
#     "ROCK": "SCISSORS",
#     "PAPER": "ROCK",
#     "SCISSORS": "PAPER"
# }

# # Score tracking
# user_score = 0
# computer_score = 0

# # Function to play the game
# def play_game(user_choice):
#     global user_score, computer_score
#     computer_choice = random.choice(choices)

#     if user_choice == computer_choice:
#         result = "It's a DRAW!"
#     elif win_conditions[user_choice] == computer_choice:
#         result = "YOU WIN! 🎉"
#         user_score += 1
#     else:
#         result = "COMPUTER WINS! 😔"
#         computer_score += 1

#     # Update score labels
#     user_score_label.config(text=f"Your Score: {user_score}")
#     computer_score_label.config(text=f"Computer Score: {computer_score}")

#     # Show result in a message box
#     messagebox.showinfo("Game Result", f"Computer chose: {computer_choice}\nYou chose: {user_choice}\n\n{result}")

# # Title Label
# title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), fg="#FFD700", bg="#222831")
# title_label.pack(pady=20)

# # Score Labels
# user_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 14, "bold"), fg="white", bg="#222831")
# user_score_label.pack()

# computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 14, "bold"), fg="white", bg="#222831")
# computer_score_label.pack()

# # Button Frame
# button_frame = tk.Frame(root, bg="#222831")
# button_frame.pack(pady=20)

# # Buttons for user choices
# rock_button = tk.Button(button_frame, text="ROCK 🪨", font=("Arial", 14), bg="#00ADB5", fg="white", width=10, height=2, command=lambda: play_game("ROCK"))
# rock_button.grid(row=0, column=0, padx=10, pady=10)

# paper_button = tk.Button(button_frame, text="PAPER 📄", font=("Arial", 14), bg="#00ADB5", fg="white", width=10, height=2, command=lambda: play_game("PAPER"))
# paper_button.grid(row=0, column=1, padx=10, pady=10)

# scissors_button = tk.Button(button_frame, text="SCISSORS ✂️", font=("Arial", 14), bg="#00ADB5", fg="white", width=10, height=2, command=lambda: play_game("SCISSORS"))
# scissors_button.grid(row=0, column=2, padx=10, pady=10)

# # Exit Button
# exit_button = tk.Button(root, text="Exit Game", font=("Arial", 14), bg="#FF5722", fg="white", width=10, height=2, command=root.quit)
# exit_button.pack(pady=20)

# # Run the main loop
# root.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
import random

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
root.configure(bg="#222831")

# Choices list
choices = ["ROCK", "PAPER", "SCISSORS"]
win_conditions = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}

# Score tracking
user_score = 0
computer_score = 0

# Function to play the game
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a DRAW!"
    elif win_conditions[user_choice] == computer_choice:
        result = "YOU WIN! 🎉"
        user_score += 1
    else:
        result = "COMPUTER WINS! 😔"
        computer_score += 1

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

    messagebox.showinfo("Game Result", f"Computer chose: {computer_choice}\nYou chose: {user_choice}\n\n{result}")

# Button animations
def on_hover(event):
    event.widget.config(bg="#FFD700")  # Change background to gold on hover

def on_leave(event):
    event.widget.config(bg="#00ADB5")  # Reset color when mouse leaves

def on_click(event):
    event.widget.config(width=11, height=1)  # Shrink on click
    root.after(150, lambda: event.widget.config(width=12, height=2))  # Expand back after 150ms

# Title Label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), fg="#FFD700", bg="#222831")
title_label.pack(pady=25)

# Score Labels
user_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 14, "bold"), fg="white", bg="#222831")
user_score_label.pack()

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 14, "bold"), fg="white", bg="#222831")
computer_score_label.pack()

# Button Frame
button_frame = tk.Frame(root, bg="#222831")
button_frame.pack(pady=20)

# Buttons with animations
buttons = []

for i, choice in enumerate(["ROCK 🪨", "PAPER 📄", "SCISSORS ✂️"]):
    button = tk.Button(
        button_frame, text=choice, font=("Arial", 14), bg="#00ADB5", fg="white",
        width=15, height=2, command=lambda c=choice.split()[0]: play_game(c)
    )
    button.grid(row=0, column=i, padx=10, pady=10)

    # 
    button.bind("<Enter>", on_hover)  # Mouse enters
    button.bind("<Leave>", on_leave)  # Mouse leaves
    button.bind("<Button-1>", on_click)  # Mouse click

    buttons.append(button)


def fade_in(index):
    if index < len(buttons):
        buttons[index].place_forget()  # Temporarily remove
        buttons[index].grid(row=0, column=index, padx=10, pady=10)  # Add back
        root.after(200, lambda: fade_in(index + 1))  # Call next button

fade_in(0)  


exit_button = tk.Button(root, text="Exit Game", font=("Arial", 14), bg="#FF5722", fg="white", width=12, height=2, command=root.quit)
exit_button.pack(pady=20)


root.mainloop()
