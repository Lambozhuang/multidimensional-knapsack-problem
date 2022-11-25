from typing import List
from common import Item, Bag, get_total_profit


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

# TODO: Neighborhood_search
