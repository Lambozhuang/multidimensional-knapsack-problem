from typing import List
from greedy_search import greedy_search
from neighborhood_search import neighborhood_search
from tabu_search import tabu_search
import util


item_num = 20
bag_num = 7

# data: ([Item.value], [Item.weight], [Bag.capacity])
data = util.generate_data(item_num, bag_num)
print(data)

# ([30, 10, 22, 24, 41, 47, 12, 8], [7, 8, 5, 1, 4, 9, 6, 2], [7, 5, 13, 11, 8]) # 184 184 194
# ([25, 6, 34, 11, 42, 10, 33, 15], [1, 6, 9, 2, 3, 8, 4, 5], [2, 6, 8, 17, 7]) # 166 176 176
# ([34, 34, 10, 40, 18, 9, 49, 45, 10, 44], [3, 2, 3, 8, 4, 7, 6, 9, 8, 7], [5, 7, 12, 10, 3])

# data = ([53, 65, 55, 61, 80, 27, 23, 34, 11, 92, 60, 18, 51, 69, 92, 24, 11, 16, 97, 83], [19, 10, 17, 16, 14, 10, 10, 19, 10, 15, 17, 11, 17, 12, 15, 12, 10, 16, 12, 19], [25, 12, 9, 27, 10, 18, 20])

# data = ([55, 82, 97, 50, 61, 75, 93, 61, 57, 68, 50, 53, 50, 89, 71, 92, 55, 76, 64, 91], [12, 19, 14, 19, 8, 11, 19, 6, 19, 18, 10, 13, 19, 19, 14, 10, 18, 13, 6, 19], [29, 7, 20, 19, 11, 23, 14])

# data = ([50, 84, 66, 52, 57, 74, 55, 71, 99, 89, 92, 50, 58, 59, 53, 71, 72, 79, 65, 62], [18, 8, 17, 15, 13, 13, 14, 9, 16, 6, 6, 12, 15, 19, 15, 11, 18, 8, 15, 17], [22, 22, 22, 10, 14, 9, 17])

# data = ([87, 98, 94, 53, 53, 79, 97, 68, 73, 69, 73, 88, 73, 77, 69, 92, 82, 74, 73, 88], [13, 12, 17, 11, 6, 13, 8, 17, 11, 5, 5, 15, 12, 7, 11, 19, 12, 18, 13, 5], [8, 29, 18, 22, 8, 8, 26])

data = ([78, 75, 92, 90, 90, 57, 73, 82, 79, 95, 70, 93, 54, 60, 73, 69, 60, 70, 66, 81], [8, 11, 9, 7, 16, 13, 19, 5, 9, 14, 15, 7, 13, 5, 8, 10, 16, 19, 17, 14], [19, 25, 12, 26, 22, 9, 11])


greedy_solution = greedy_search(data)
neighborhood_solution = neighborhood_search(data)
tabu_solution = tabu_search(data, tabu_list_length=(item_num / 2), tabu_max_iter=100)

print(f"Greedy: {greedy_solution}")
print(f"Neighborhood: {neighborhood_solution}")
print(f"Tabu search: {tabu_solution}")
