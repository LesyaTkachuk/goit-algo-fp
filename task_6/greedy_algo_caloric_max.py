from constants import FOOD_ITEMS


def greedy_algo_caloric_max(items, budget=100):
    # make a list from food items dictionary
    items_arr = list(items.items())
    # sort food items array by the ratio of cost/calories
    items_arr.sort(key=lambda x: x[1]["cost"] / x[1]["calories"])

    total_calories = 0
    total_budget = 0
    food = []

    # move through sorted array and check if item cost is acceptable for the budget amount
    for item in items_arr:
        if budget >= item[1]["cost"]:
            budget -= item[1]["cost"]
            total_calories += item[1]["calories"]
            total_budget += item[1]["cost"]
            food.append(item[0])
    # form a tuple with the obtained results
    return (total_calories, total_budget, food)


if __name__ == "__main__":
    total_calories, total_budget, food = greedy_algo_caloric_max(FOOD_ITEMS)
    print("*" * 50)
    print("Greedy algorithm caloric maximisation task solving")
    print("-" * 50)
    print(f"{'Calories amount':<20} | {'Money spent':<20}")
    print(f"{total_calories:<20} | {total_budget:<20}")
    print("-" * 50)
    [print(item) for item in food]
    print("*" * 50)
