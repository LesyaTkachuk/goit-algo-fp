import turtle


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


if __name__ == "__main__":
    draw_pythagoras_tree(8)
