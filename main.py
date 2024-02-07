from task_2.pythagoras_tree import draw_pythagoras_tree
from utils import print_red
from utils.constants import BLUE, RESET


def main():
    recursion_number = input(
        BLUE + "To draw the Pythagorath tree enter the number of recursion: " + RESET
    )
    try:
        draw_pythagoras_tree(int(recursion_number))
    except ValueError:
        print_red("\033[91m" + "Recursion number should be an integer!" + "\033[0m")
        main()


if __name__ == "__main__":
    main()
