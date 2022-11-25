import numpy


items = [(1, 12), (6, 38), (3, 18), (7, 39), (3, 14), (8, 27), (8, 24), (7, 8)]
bags = [11, 7, 6, 6, 6]

weights = [item[0] for item in items]
profits = [item[1] for item in items]
benefits = [profits[i] / weights[i] for i in range(len(items))]

# print(weights)
# print(profits)
# print(benefits)

benefits.sort(reverse=True)
benefits = numpy.array(benefits)
sorted_items_index = numpy.argsort(benefits)[::-1][:len(benefits)] # descending argsort

print(f"sorted item index: {sorted_items_index}")

def greedy_search():
    total_profits = 0
    items_in_bags = [-1] * len(items)
    for index in sorted_items_index:
        for j in range(len(bags)):
            if bags[j] >= weights[index]:
                items_in_bags[index] = j
                total_profits += profits[index]
                bags[j] -= weights[index]
                break

    print(f"total profits: {total_profits}")
    print(f"item in bags: {items_in_bags}")

def neighborhood_search():
    pass
