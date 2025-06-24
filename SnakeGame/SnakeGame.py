import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
DELAY = 100  # milliseconds

# Setup
window = tk.Tk()
window.title("Snake Game || Devloper by Ramakant Chaudhari ")
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="#CFECEC")
canvas.pack()

# Game variables
snake = [(5, 5), (4, 5), (3, 5)]
direction = "Right"
food = None
running = True
score = 0

def draw_cell(x, y, color):
    x1 = x * CELL_SIZE
    y1 = y * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

def draw_circle(x, y, color):
    x1 = x * CELL_SIZE + 2
    y1 = y * CELL_SIZE + 2
    x2 = x1 + CELL_SIZE - 4
    y2 = y1 + CELL_SIZE - 4
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")

def draw_snake():
    for i, (x, y) in enumerate(snake):
        if i == 0:
            draw_cell(x, y, "red")
        else:
            draw_cell(x, y, "#F67280")


def place_food():
    global food
    while True:
        x = random.randint(0, WIDTH // CELL_SIZE - 1)
        y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        if (x, y) not in snake:
            food = (x, y)
            break

def change_direction(event):
    global direction
    new_dir = event.keysym
    opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    if new_dir in opposites and opposites[new_dir] != direction:
        direction = new_dir

def game_over():
    global running
    running = False
    canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="Black", font=("Arial", 30))

def move_snake():
    global snake, food, running, score

    if not running:
        return

    head_x, head_y = snake[0]
    dx, dy = 0, 0
    if direction == "Up": dy = -1
    elif direction == "Down": dy = 1
    elif direction == "Left": dx = -1
    elif direction == "Right": dx = 1

    new_head = (head_x + dx, head_y + dy)

    if (new_head in snake or
        new_head[0] < 0 or new_head[1] < 0 or
        new_head[0] >= WIDTH // CELL_SIZE or
        new_head[1] >= HEIGHT // CELL_SIZE):
        game_over()
        return

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        place_food()
    else:
        snake.pop()

    draw_game()
    window.after(DELAY, move_snake)

def draw_game():
    canvas.delete("all")
    canvas.create_text(50, 10, text=f"Score: {score}", fill="Black", font=("Arial", 14))
    draw_snake()
    if food:
        draw_circle(food[0], food[1], "blue")

# Start game
place_food()
draw_game()
window.bind("<KeyPress>", change_direction)
move_snake()
window.mainloop()
