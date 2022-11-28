from typing import List, Tuple
import util
import random
import copy


def neighborhood_search(data: Tuple[List[int], List[int], List[int]]):

    (items, bags) = util.process_data(data)

    items.sort(key=lambda x: x.benefit, reverse=True)
    bags.sort(key=lambda x: x.capacity, reverse=False)

    # Greedy search
    for item in items:
        for bag in bags:
            if bag.capacity_left >= item.weight:
                bag.add_item(item)
                break

    util.sync(bags, items)
    best_solution = [item.bag for item in items]
    best_total_profit = util.get_total_profit_of_bags(bags)
    best_bags = copy.deepcopy(bags)
    best_items = copy.deepcopy(items)

    # Neighborhood search
    local_optima_flag = False
    while not local_optima_flag:
        continue_flag = False
        item_to_change = util.get_best_leftover(items)
        if item_to_change == None:
            print("Neighborhood search: No item leftover. \
                Best solution has been found.")
            return best_total_profit

        last_bags = copy.deepcopy(bags)
        last_items = copy.deepcopy(items)
        for i in range(len(bags)):
            bag = bags[i]
            next_bag = bags[0 if i == len(bags) - 1 else i + 1]
            rotate = False       
            # Select two items in two bags to rotate
            for item_1 in bag.items:
                if rotate:
                    break
                for item_2 in next_bag.items:
                    if rotate:
                        break
                    if bag.capacity_left + item_1.weight >= item_to_change.weight \
                        and next_bag.capacity_left + item_2.weight >= item_1.weight:
                        rotate = True
                        temp_item = item_2
                        next_bag.remove_item(item_2)
                        next_bag.add_item(item_1)
                        bag.remove_item(item_1)
                        bag.add_item(item_to_change)
                        item_to_change = temp_item

            util.sync(bags, items)
            for item in items:
                if item.bag == -1:
                    for bag in bags:
                        if bag.capacity_left >= item.weight:
                            bag.add_item(item)
                            break

            util.sync(bags, items)
            current_solution = [item.bag for item in items]
            current_total_profit = util.get_total_profit_of_bags(bags)
            print(f"i: {i}", end=" ")
            print(f"rotate: {rotate}", end=" ")
            print(f"current_total_profit: {current_total_profit}")

            # Update best solution
            if current_total_profit > best_total_profit:
                best_solution = current_solution
                best_total_profit = current_total_profit
                best_bags = copy.deepcopy(bags)
                best_items = copy.deepcopy(items)
                print(f"update best_total_profit: {best_total_profit}")
                continue_flag = True

            # Reset bags and items
            bags = copy.deepcopy(last_bags)
            items = copy.deepcopy(last_items)
            util.sync(bags, items)
            item_to_change = util.get_best_leftover(items)

        print(f"continue: {continue_flag}")
        # Enter next neighborhood starting point
        if continue_flag:
            bags = copy.deepcopy(best_bags)
            items = copy.deepcopy(best_items)
        else:
            local_optima_flag = True
    print("Neighborhood search done.")
    print()
    return best_total_profit
