from typing import List
from greedy_search import greedy_search
from neighborhood_search import neighborhood_search
from tabu_search import tabu_search
import util


# data: ([Item.value], [Item.weight], [Bag.capacity])
data = ([78, 75, 92, 90, 90, 57, 73, 82, 79, 95,\
     70, 93, 54, 60, 73, 69, 60, 70, 66, 81],\
     [8, 11, 9, 7, 16, 13, 19, 5, 9, 14,\
     15, 7, 13, 5, 8, 10, 16, 19, 17, 14],\
     [19, 25, 12, 26, 22, 9, 11])

greedy_solution = greedy_search(data)
neighborhood_solution = neighborhood_search(data)
tabu_solution = tabu_search(data)
print(f"Greedy method total profit: {greedy_solution}")
print(f"Neighborhood search method total profit: {neighborhood_solution}")
print(f"Tabu search method total profit: {tabu_solution}")
print()

