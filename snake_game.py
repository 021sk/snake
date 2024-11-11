from tkinter import *
from random import randint


# ------------------------------------
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        for i in range(BODY_SIZE):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tags='snake')
            self.squares.append(square)


class Food:
    def __init__(self):
        x = randint(0, GAME_WIDTH // SPACE_SIZE - 1) * SPACE_SIZE
        y = randint(0, GAME_HEIGHT // SPACE_SIZE - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')


def restart_program():
    pass


def change_direction():
    pass


def next_turn(snake, food):
    x, y = snake.coordinates[0]


# ------------------------------------

GAME_WIDTH = 700
BODY_SIZE = 4
GAME_HEIGHT = 700
SPACE_SIZE = 25
SLOWNESS = 150
SNAKE_COLOUR = "yellow"
BACKGROUND_COLOR = "black"
FOOD_COLOR = "red"
score = 0
direction = "down"

# --------------------------------------

window = Tk()
window.title("SnakeGame")
window.resizable(False, False)

label = Label(window, text=f"Score: {score}", font=("Arial", 30))
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

restart = Button(window, text="restart", fg="green", command=restart_program, font=("Arial"), bg=BACKGROUND_COLOR)
restart.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width / 2) - int(window_width / 2)
y = int(screen_height / 2) - int(window_height / 2)
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# print(window_width, window_height)
# print(screen_width, screen_height)
window.bind('<Left>', lambda event: change_direction("left"))
window.bind('<Right>', lambda event: change_direction("right"))
window.bind('<Down>', lambda event: change_direction("down"))
window.bind('<Up>', lambda event: change_direction("up"))
snake = Snake()
food = Food()
next_turn(snake, food)
window.mainloop()
