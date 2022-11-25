from typing import List
from common import Item, Bag, get_total_profit_of_items


input_items = [(1, 12), (6, 38), (3, 18), (7, 39), (3, 14), (8, 27), (8, 24), (7, 8)]
input_bags = [11, 7, 6, 6, 6]

items: List[Item] = []
for i in range(len(input_items)):
    items.append(Item(id=i, value=input_items[i][1], weight=input_items[i][0]))

bags: List[Bag] = []
for i in range(len(input_bags)):
    bags.append(Bag(id=i, capacity=input_bags[i]))

items.sort(key=lambda x: x.benefit, reverse=True)
bags.sort(key=lambda x: x.capacity, reverse=True)

best_solution: List[int] = []
best_total_profit = 0

# Get the first solution with greedy search
for item in items:
    for bag in bags:
        if bag.capacity_left >= item.weight:
            item.bag = bag.id
            bag.decrese_capacity(item.weight)
            break

best_solution = [item.bag for item in items]
best_total_profit = get_total_profit_of_items(items=items)
print(best_solution)
print(best_total_profit)

for bag in bags:
    bag.reset_capacity()

# Neighborhood_search
flag = True
while(flag): # Search loop until local optima
    # TODO: Define the neighborhood
    pass
