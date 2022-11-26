from typing import List
from greedy_search import greedy_search
import util


item_num = 8
bag_num = 5

# data: ([Item.value], [Item.weight], [Bag.capacity])
data = util.generate_data(item_num, bag_num)
# print(data)

# ([30, 10, 22, 24, 41, 47, 12, 8], [7, 8, 5, 1, 4, 9, 6, 2], [7, 5, 13, 11, 8])
# ([25, 6, 34, 11, 42, 10, 33, 15], [1, 6, 9, 2, 3, 8, 4, 5], [2, 6, 8, 17, 7])

data = ([25, 6, 34, 11, 42, 10, 33, 15], [1, 6, 9, 2, 3, 8, 4, 5], [2, 6, 8, 17, 7])

print(greedy_search(data))
