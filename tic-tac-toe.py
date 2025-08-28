#importing Packages from tkinter
from tkinter import *
from tkinter import messagebox 

Player1 = 'X'
stop_game = False

def clicked(r, c):
    global Player1, stop_game

    if states[r][c] == 0 and not stop_game:
        b[r][c].configure(text=Player1)
        states[r][c] = Player1
        Player1 = 'O' if Player1 == 'X' else 'X'  # Toggle player
        check_if_win()

def check_if_win():
    global stop_game

    # Check rows and columns
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:  # Row check
            stop_game = True
            messagebox.showinfo("Winner", f"{states[i][0]} Won!")
            return

        if states[0][i] == states[1][i] == states[2][i] != 0:  # Column check
            stop_game = True
            messagebox.showinfo("Winner", f"{states[0][i]} Won!")
            return

    # Check diagonals
    if states[0][0] == states[1][1] == states[2][2] != 0:
        stop_game = True
        messagebox.showinfo("Winner", f"{states[0][0]} Won!")
        return

    if states[0][2] == states[1][1] == states[2][0] != 0:
        stop_game = True
        messagebox.showinfo("Winner", f"{states[0][2]} Won!")
        return

    # Check for a tie
    if all(states[i][j] != 0 for i in range(3) for j in range(3)) and not stop_game:
        stop_game = True
        messagebox.showinfo("Tie", "It's a tie!")

# Create window
root = Tk()
root.title("Tic Tac Toe") 
root.resizable(0, 0)

# Create button grid
b = [[None for _ in range(3)] for _ in range(3)]
states = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3): 
        b[i][j] = Button(root, height=4, width=8, font=("Helvetica", "20"),
                         command=lambda r=i, c=j: clicked(r, c))
        b[i][j].grid(row=i, column=j)

root.mainloop()
