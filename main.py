from task_2.pythagoras_tree import draw_pythagoras_tree
from utils import print_red


def main():
    recursion_number = input(
        "\033[38;2;0;100;200m"
        + "To draw the Pythagorath tree enter the number of recursion: "
        + "\033[0m"
    )
    try:
        draw_pythagoras_tree(int(recursion_number))
    except ValueError:
        print_red("\033[91m" + "Recursion number should be an integer!" + "\033[0m")
        main()


if __name__ == "__main__":
    main()
