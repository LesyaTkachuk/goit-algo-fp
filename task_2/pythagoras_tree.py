import turtle

from print_red import print_red

BLUE = "\033[38;2;0;100;200m"
RESET = "\033[0m"


def pythagoras_tree(level, branch_length=100, angle=45, width_factor=0.75):
    if level == 0:
        return
    else:
        # Draw the main branch
        turtle.forward(branch_length)
        turtle.left(angle)

        # Recursive call for the right subtree
        pythagoras_tree(level - 1, branch_length * width_factor, angle, width_factor)

        turtle.right(2 * angle)

        # Recursive call for the left subtree
        pythagoras_tree(level - 1, branch_length * width_factor, angle, width_factor)

        turtle.left(angle)
        turtle.backward(branch_length)


def draw_pythagoras_tree(n):
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("green")
    turtle.title("Pythagoras Tree Fractal")

    turtle.left(90)
    turtle.up()
    turtle.backward(300)
    turtle.down()

    pythagoras_tree(
        n,
        150,
        45,
    )

    turtle.hideturtle()
    turtle.done()


def ask_level_of_recursion():
    recursion_number = input(
        BLUE + "To draw the Pythagorath tree enter the number of recursion: " + RESET
    )
    try:
        draw_pythagoras_tree(int(recursion_number))
    except ValueError:
        print_red("\033[91m" + "Recursion number should be an integer!" + "\033[0m")
        ask_level_of_recursion()


if __name__ == "__main__":
    # draw_pythagoras_tree(6)
    ask_level_of_recursion()
    