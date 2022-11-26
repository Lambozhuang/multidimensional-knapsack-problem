from typing import List, Tuple
import random
from common import Item, Bag


def generate_data(item_num: int, bag_num: int):
    item_values = random.sample(range(5, 50), item_num)
    item_weights = random.sample(range(1, 10), item_num)
    bag_capacity = random.sample(range(2, 20), bag_num)

    return (item_values, item_weights, bag_capacity)

# data: ([Item.value], [Item.weight], [Bag.capacity])
def process_data(data: Tuple[List[int], List[int], List[int]]) -> Tuple[List[Item], List[Bag]]: 
    items: List[Item] = []
    bags: List[Bag] = []

    for i in range(len(data[0])):
        items.append(Item(i, data[0][i], data[1][i]))

    for i in range(len(data[2])):
        bags.append(Bag(i, data[2][i]))

    return (items, bags)

def get_total_profit_of_items(items: List[Item]):
    total_profit = 0
    for item in items:
        if item.bag != -1:
            total_profit += item.value
    return total_profit

def get_total_profit(list_of_profit: List[int]):
    total_profit = 0
    for profit in list_of_profit:
        total_profit += profit
    return total_profit