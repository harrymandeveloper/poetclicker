# Imports a random module
import random

# Imports a random integer generator
from random import randint

# Gives us a sprite - an image of the poet that we want to click on
harjo = Actor("harjo")

# Clear the screen and add a sprite


def draw():
    screen.clear()
    harjo.draw()


# Pick a position for the poet to be placed on the screen
def place_harjo():
    harjo.x = randint(10, 790)
    harjo.y = randint(10, 590)


# Lines of poetry that need to be stored in memory
harjo_lines = ["We were running out of breath, as we ran out to meet ourselves.", "We were surfacing the edge of our ancestors’ fights, and ready to strike.",
               "Easy if you played pool and drank to remember to forget.", "some of us could sing so we drummed a fire-lit pathway up to those starry stars."]


def random_harjo_line_chooser():
    print(random.choice(harjo_lines))


# Calls the place_harjo function - so colon not required when calling the function
place_harjo()


# Score
counter = 0

# Successful click on a poet - behaviour


def on_mouse_down(pos):
    if harjo.collidepoint(pos):
        global counter
        counter += 1
        random_harjo_line_chooser()
        place_harjo()

# Display the score in the console / Terminal
        print(f"Your score is {counter}")

    else:
        print("You missed! Game Over \nThis is the way the world ends \nnot with a bang, but a whimper")
        quit()
