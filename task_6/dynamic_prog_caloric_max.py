from constants import FOOD_ITEMS, BLUE, RESET


def dynamic_prog_caloric_max(items, budget=100, print_table=False):
    items_amount = len(items)
    # make a list from food items dictionary
    items_arr = list(items.items())
    # sort food items array by the cost amount
    items_arr.sort(key=lambda x: x[1]["cost"])

    # create a table T to store optimal solution for each subtask
    T = [[0 for _ in range(budget + 1)] for i in range(items_amount + 1)]
    selected_items = [[[] for _ in range(budget + 1)] for i in range(items_amount + 1)]

    # build the table
    for item in range(items_amount + 1):
        for budg in range(budget + 1):
            if item == 0 or budg == 0:
                T[item][budg] = 0
            elif items_arr[item - 1][1]["cost"] <= budg:
                if (
                    items_arr[item - 1][1]["calories"]
                    + T[item - 1][budg - items_arr[item - 1][1]["cost"]]
                    > T[item - 1][budg]
                ):
                    T[item][budg] = (
                        items_arr[item - 1][1]["calories"]
                        + T[item - 1][budg - items_arr[item - 1][1]["cost"]]
                    )
                    selected_items[item][budg] = selected_items[item - 1][
                        budg - items_arr[item - 1][1]["cost"]
                    ] + [items_arr[item - 1][0]]
                else:
                    T[item][budg] = T[item - 1][budg]
                    selected_items[item][budg] = selected_items[item - 1][budg]
            else:
                T[item][budg] = T[item - 1][budg]
                selected_items[item][budg] = selected_items[item - 1][budg]

    if print_table:
        # visualisation of the table with the optimal result for each subtask
        for index, el in enumerate(T):
            if index == 0:
                print(f"{BLUE}{'No item':-<10}{RESET}: {el}")
            else:
                print(f"{BLUE}{items_arr[index-1][0] :-<10}{RESET} : {el}")

    return T[items_amount][budget], selected_items[items_amount][budget]


if __name__ == "__main__":
    calories, food_items = dynamic_prog_caloric_max(FOOD_ITEMS, 100)
    print("*" * 60)
    print("Dynamic programming caloric maximisation task solving")
    print("-" * 60)
    print(f"Maximum calories amount is {calories}")
    print("-" * 50)
    [print(item) for item in food_items]
    print("*" * 50)
