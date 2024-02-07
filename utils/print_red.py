def print_red(message):
    red = "\033[91m"  # ANSI escape code for red color
    reset_color = "\033[0m"  # Reset color to default

    print(red + message + reset_color)
