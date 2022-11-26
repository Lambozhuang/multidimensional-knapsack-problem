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
        return '{' + str(self.id) + ', ' + str(self.benefit) + '}'

class Bag:
    def __init__(self, id, capacity) -> None:
        self.id = id
        self.capacity = capacity
        self.capacity_left = capacity

    def __repr__(self):
        return '{' + str(self.id) + ', ' + str(self.capacity) + '}'

    def decrese_capacity(self, amount: int):
        if self.capacity_left < amount:
            print("Error: exceed bag capacity")
            exit()
        self.capacity_left -= amount

    def reset_capacity(self):
        self.capacity_left = self.capacity


