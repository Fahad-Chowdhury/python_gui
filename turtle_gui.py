from turtle import Turtle, Screen
from random import random, randint, choice

class TurtleGui:

    def __init__(self):
        self.turtle = Turtle()

    def draw_dashed_line(self, no_of_dashes, size_of_dashes):
        """ Draws a dashed line with given no_of_dashes and given size_of_dashes. """
        for _ in range(no_of_dashes):
            self.turtle.pendown()
            self.turtle.forward(size_of_dashes)
            self.turtle.penup()
            self.turtle.forward(size_of_dashes)

    def exit_program_on_mouse_click(self):
        """ Exit program on mouse click. """
        my_screen = Screen()
        my_screen.exitonclick()

    def set_random_color(self):
        """ Sets a random pen color for lines. """
        r = random()
        g = random()
        b = random()
        self.turtle.color(r, g, b)

    def draw_shape(self, no_of_sides, length=100):
        """ Draws a shape of side given by 'no_of_sides' and of length of each side. """
        angle = 360 / no_of_sides
        for _ in range(no_of_sides):
            self.turtle.forward(length)
            self.turtle.right(angle)

    def draw_shapes(self):
        """ Draws shapes from triangle to decagon and each of one random color. """
        for sides in range(3, 11):
            self.set_random_color()
            self.draw_shape(sides)

    def draw_random_walk(self, min_steps=20, max_steps=200, length_of_step=50):
        """ Draw a random walk of random length in range between min and max number of steps
        and of given length of each step. """
        no_of_steps = randint(min_steps, max_steps)
        directions = (0, 90, 180, 270)
        self.turtle.pensize(15)
        self.turtle.speed(0)
        for _ in range(no_of_steps):
            self.set_random_color()
            self.turtle.forward(length_of_step)
            self.turtle.setheading(choice(directions))

    def _draw_spirograph(self, shift_degrees=5):
        """ Draw a spirograph. """
        self.turtle.speed(0)
        total_circles = int(360 / shift_degrees)
        for _ in range(0, total_circles):
            self.set_random_color()
            self.turtle.circle(100)
            self.turtle.right(shift_degrees)


def get_user_choice():
    ''' Gets a choice from user to draw selected object. Returns selcted
    integer value if selected choice is valid, else returns 0. '''
    print('Choose an option (1 to 3):')
    print('1. Spirograph')
    print('2. Random Walk')
    print('3. Draw shapes')
    print('4. Draw dashed line')
    print('Any other character to exit.')
    choice = input(f"Your choice?: ")
    if choice.isnumeric() and int(choice) in range(1, 5):
        return int(choice)
    return 0


def main():
    choice = get_user_choice()
    turtle = TurtleGui()
    match choice:
        case 1:
            turtle._draw_spirograph()
        case 2:
            turtle.draw_random_walk()
        case 3:
            turtle.draw_shapes()
        case 4:
            turtle.draw_dashed_line(15, 10)
    print('Click on screen to close the drawing.')
    turtle.exit_program_on_mouse_click()


if __name__ == "__main__":
    main()
