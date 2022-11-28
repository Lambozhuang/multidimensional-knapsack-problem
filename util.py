from typing import List, Tuple
import random
from common import Item, Bag


def generate_data(item_num: int, bag_num: int):
    item_values = [random.randrange(50, 100, 1) for i in range(item_num)]
    item_weights = [random.randrange(5, 20, 1) for i in range(item_num)]
    bag_capacity = [random.randrange(5, 30, 1) for i in range(bag_num)]

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

def get_total_profit_of_bags(bags: List[Bag]):
    total_profit = 0
    for bag in bags:
        for item in bag.items:
            total_profit += item.value
    return total_profit

def sync(bags: List[Bag], items: List[Item]):
    for item in items:
        item.bag = -1
    for bag in bags:
        if len(bag.items) == 0:
            continue
        for item in bag.items:
            for _item in items:
                if item.id == _item.id:
                    item.bag = bag.id
                    _item.bag = bag.id

def get_best_leftover(items: List[Item]):
    for item in items:
        if item.bag == -1:
            return item
    return None

def get_random_leftover(items: List[Item]):
    leftovers = []
    for item in items:
        if item.bag == -1:
            leftovers.append(item)
    return random.sample(leftovers, 1)[0]

def is_in_tabu_list(tabu_list: List[int], total_profit: int):
    for i in tabu_list:
        if i == total_profit:
            return True
    return False

def get_best_in_tabu_list(tabu_list: List[int]):
    best = 0
    for i in tabu_list:
        if i >= best:
            best = i
    return best
