from typing import List, Tuple
import util


def greedy_search(data: Tuple[List[int], List[int], List[int]]) -> int:

    (items, bags) = util.process_data(data)

    items.sort(key=lambda x: x.benefit, reverse=True)
    bags.sort(key=lambda x: x.capacity, reverse=False)

    for item in items:
        for bag in bags:
            if bag.capacity_left >= item.weight:
                bag.add_item(item)
                break
    
    print("Greedy search done.")
    print()
    return util.get_total_profit_of_items(items)
