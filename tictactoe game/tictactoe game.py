import tkinter as tk
from tkinter import messagebox
import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "X"
winner = None
gameRunning = True

# GUI setup
root = tk.Tk()
root.title("Tic Tac Toe - Player vs Computer || Devloper by Ramakant Chaudhari")
root.geometry("400x450")
buttons = []


def playerInput(index):
    global currentPlayer
    if board[index] == "-" and gameRunning:
        board[index] = currentPlayer
        updateButtons()
        if checkWin() or checkTie(board):
            return
        switchPlayer()
        root.after(100, computer)

def checkHorizontal(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            winner = board[i]
            return (i, i+1, i+2)
    return False

def checkRow(board):
    global winner
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            winner = board[i]
            return (i, i+3, i+6)
    return False

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return (0, 4, 8)
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return (2, 4, 6)
    return False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        showResult("It's a tie!")
        gameRunning = False
        return True
    return False

def checkWin():
    global gameRunning
    for check in [checkHorizontal, checkRow, checkDiagonal]:
        result = check(board)
        if result:
            gameRunning = False
            showResult(f"The winner is {winner}!", result)
            return True
    return False

def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

def computer():
    global currentPlayer
    if currentPlayer == "O" and gameRunning:
        position = random.randint(0, 8)
        while board[position] != "-":
            position = random.randint(0, 8)
        board[position] = "O"
        updateButtons()
        if checkWin() or checkTie(board):
            return
        switchPlayer()

# --- GUI Specific ---

def updateButtons():
    for i in range(9):
        buttons[i].config(text=board[i], state=tk.DISABLED if board[i] != "-" else tk.NORMAL)

def showResult(message, win_cells=None):
    if win_cells:
        for i in win_cells:
            buttons[i].config(bg="lightgreen")
    messagebox.showinfo("Game Over", message)
    disableButtons()

def disableButtons():
    for btn in buttons:
        btn.config(state=tk.DISABLED)

def resetGame():
    global board, currentPlayer, winner, gameRunning
    board = ["-"] * 9
    currentPlayer = "X"
    winner = None
    gameRunning = True
    for btn in buttons:
        btn.config(text="-", state=tk.NORMAL, bg="SystemButtonFace")

# --- UI Layout ---

tk.Label(root, text="Tic Tac Toe", font=("Arial", 22, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="-", font=('Arial', 20), width=5, height=2,
                    command=lambda i=i: playerInput(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

tk.Button(root, text="Reset", font=("Arial", 14), bg="#00fffb", fg="black", command=resetGame).pack(pady=15)

root.mainloop()
