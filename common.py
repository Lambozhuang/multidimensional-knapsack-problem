from typing import List


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

class Bag:
    def __init__(self, id, capacity) -> None:
        self.id = id
        self.capacity = capacity
        self.capacity_left = capacity

    def decrese_capacity(self, amount: int):
        if self.capacity_left < amount:
            print("Error: exceed bag capacity")
            exit()
        self.capacity_left -= amount

def get_total_profit(items: List[Item]):
    total_profit = 0
    for item in items:
        if item.bag != -1:
            total_profit += item.value
    return total_profit