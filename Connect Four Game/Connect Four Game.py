import tkinter as tk
from tkinter import messagebox
import random

ROWS = 6
COLUMNS = 7
CELL_SIZE = 100
PLAYER_COLORS = ["#6495ED", "#00FFFF"]

# Game state
turn = 0  # 0 for human (Player 1), 1 for computer (Player 2)
board = [["" for _ in range(COLUMNS)] for _ in range(ROWS)]
canvas_cells = []
buttons = []
canvas = None
game_over = False

def create_board(root):
    global canvas
    # Top row buttons
    button_frame = tk.Frame(root)
    button_frame.pack()
    for col in range(COLUMNS):
        btn = tk.Button(button_frame, text="↓", font=("Arial", 20), command=lambda c=col: handle_move(c))
        btn.grid(row=0, column=col)
        buttons.append(btn)

    # Canvas for grid
    canvas = tk.Canvas(root, width=COLUMNS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="#FFFF66")
    canvas.pack()

    for row in range(ROWS):
        row_cells = []
        for col in range(COLUMNS):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            oval = canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="white")
            row_cells.append(oval)
        canvas_cells.append(row_cells)

def handle_move(col):
    global turn, game_over
    if game_over or turn != 0:
        return

    row = get_next_open_row(col)
    if row is None:
        return

    place_piece(row, col, PLAYER_COLORS[turn])

    if check_game_end(row, col, PLAYER_COLORS[turn]):
        return

    turn = 1
    root.after(500, computer_move)

def computer_move():
    global turn, game_over
    if game_over:
        return

    valid_columns = [c for c in range(COLUMNS) if get_next_open_row(c) is not None]
    if not valid_columns:
        return

    col = random.choice(valid_columns)
    row = get_next_open_row(col)

    place_piece(row, col, PLAYER_COLORS[turn])

    if check_game_end(row, col, PLAYER_COLORS[turn]):
        return

    turn = 0

def place_piece(row, col, color):
    board[row][col] = color
    canvas.itemconfig(canvas_cells[row][col], fill=color)

def get_next_open_row(col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == "":
            return row
    return None

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def is_draw():
    return all(board[0][col] != "" for col in range(COLUMNS))

def check_game_end(row, col, color):
    global game_over
    if check_win(row, col, color):
        winner = "You" if color == "#6495ED" else "Computer"
        messagebox.showinfo("Game Over", f"{winner} wins!")
        disable_buttons()
        game_over = True
        return True
    elif is_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        disable_buttons()
        game_over = True
        return True
    return False

def check_win(row, col, color):
    def count(dx, dy):
        count = 1
        for direction in [1, -1]:
            r, c = row, col
            while True:
                r += dy * direction
                c += dx * direction
                if 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == color:
                    count += 1
                else:
                    break
        return count

    for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        if count(dx, dy) >= 4:
            return True
    return False

# Run the game
root = tk.Tk()
root.title("Connect Four Game || Devlopers By Ramakant Chaudhari ")
create_board(root)
root.mainloop()
