from typing import List, Tuple
import random


class Item:
    def __init__(self, id, value, weight) -> None:
        self.id = id
        self.value = value
        self.weight = weight
        if self.weight == 0:
            print("Invalid weight.")
            exit()
        self.benefit = self.value / self.weight
        self.bag = -1

    def __repr__(self):
        return '{id: ' + str(self.id) + \
            ', benefit: ' + str(round(self.benefit, 2)) + \
            ', bag: ' + str(self.bag) + '}'

class Bag:
    def __init__(self, id, capacity) -> None:
        self.id = id
        self.capacity = capacity
        self.capacity_left = capacity
        self.items: List[Item] = []

    def __repr__(self):
        return '{id: ' + str(self.id) +\
             ', capacity_left: ' + str(self.capacity_left) + '}'

    def add_item(self, item: Item):
        item.bag = self.id
        self.items.append(item)
        if self.capacity_left < item.weight:
            print("Error: exceed bag capacity")
            exit()
        self.capacity_left -= item.weight

    def remove_item(self, item: Item):
        index = -1
        for i in range(len(self.items)):
            if self.items[i].id == item.id:
                index = i
                break
        if index == -1:
            print("Error: Item not found")
            exit()
        _item = self.items.pop(index)
        _item.bag = -1
        self.capacity_left += _item.weight
        if self.capacity_left > self.capacity:
            print("Error: wrong capacity")
            exit()

    def pop_item(self):
        item_to_pop = self.items.pop()
        self.capacity_left += item_to_pop.weight
        item_to_pop.bag = -1
        return item_to_pop

    def reset_capacity(self):
        self.capacity_left = self.capacity

    def print_items(self):
        print(self.items)


