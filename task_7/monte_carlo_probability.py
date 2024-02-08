import random
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

ANALITICAL_RESULTS = {
    2: 0.0278,
    3: 0.0556,
    4: 0.0833,
    5: 0.1111,
    6: 0.1389,
    7: 0.1667,
    8: 0.1389,
    9: 0.1111,
    10: 0.0833,
    11: 0.0556,
    12: 0.0278,
}


def monte_carlo_probability(n):
    # initialise default dict for results storage
    counts = defaultdict(int)

    # make simulation of two dices sum for n number of experiments
    for _ in range(n):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)

        # add result of two dices into default dict
        counts[dice_one + dice_two] += 1

    items = list(counts.items())
    items.sort(key=lambda x: x[0])

    # form dictionary with probabilities for each dices sum
    probabilities = {key: count / n for key, count in items}

    return probabilities


def draw_bar(probabilities, title="Probabilities bar"):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    # perform calculations using Monte-Carlo method for different number of experiments
    result_36 = monte_carlo_probability(36)
    result_1000 = monte_carlo_probability(1_000)
    result_100000 = monte_carlo_probability(100_000)
    # print the results in the table
    print("*" * 100)
    print(f"{'Two dices sum':^15} | {'Probability':^60}")
    print("-" * 100)
    print(
        f"{'':<15} | {'36 experiments':^15} | {'1000 experiments ':^17} | {'100000 exp.':^15} | {'Analitical results':^15}"
    )
    print("-" * 100)
    for sum, prob in result_1000.items():
        print(
            f"{sum:^15} | {prob:^15.2%} | {result_1000[sum]:^17.2%} | {result_100000[sum]:^15.2%} | {ANALITICAL_RESULTS[sum]:^15.2%}"
        )
    print("*" * 100)

    # draw bar for obtained probabilities
    draw_bar(result_36, "Probability distribution for 36 experiments")
    draw_bar(result_1000, "Probability distribution for 1000 experiments")
    draw_bar(result_100000, "Probability distribution for 100000 experiments")
