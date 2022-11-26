from typing import List, Tuple
import util
import random
import copy


def neighborhood_search(data: Tuple[List[int], List[int], List[int]]):

    (items, bags) = util.process_data(data)

    items.sort(key=lambda x: x.benefit, reverse=True)
    bags.sort(key=lambda x: x.capacity, reverse=False)

    best_solution: List[int] = []
    best_total_profit = 0

    # Get the first solution with greedy search
    for item in items:
        for bag in bags:
            if bag.capacity_left >= item.weight:
                bag.add_item(item)
                break

    best_solution = [item.bag for item in items]
    best_total_profit = util.get_total_profit_of_bags(bags)
    # print(best_solution)
    # print(best_total_profit)

    # Neighborhood search
    local_optima_flag = False
    while not local_optima_flag:

        continue_flag = False
        # util.reset_capacity(bags)
        item_to_change = util.get_best_leftover(items)

        if item_to_change == None:
            print("Neighborhood search: No item leftover. Best solution has been found.")
            # print(f"solution: {best_solution}")
            # print(f"profit: {best_total_profit}")
            return best_total_profit

        # random.shuffle(bags)

        last_bags = copy.deepcopy(bags)
        last_items = copy.deepcopy(items)
        util.update_item_list(bags, items)

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
                        util.update_item_list(bags, items)
            for item in items:
                if item.bag == -1:
                    for bag in bags:
                        if bag.capacity_left >= item.weight:
                            bag.add_item(item)
                            break
            
            current_solution = [item.bag for item in items]
            current_total_profit = util.get_total_profit_of_bags(bags)
            print(f"i: {i}", end=" ")
            print(f"rotate: {rotate}", end=" ")
            print(f"current_total_profit: {current_total_profit}")
            # print(f"current_solution: {current_solution}")

            if current_total_profit > best_total_profit:
                best_total_profit = current_total_profit
                best_solution = current_solution
                print(f"update best_total_profit: {best_total_profit}")
                better_bags = copy.deepcopy(bags)
                better_items = copy.deepcopy(items)
                continue_flag = True

            bags = copy.deepcopy(last_bags)
            items = copy.deepcopy(last_items)
            util.update_item_list(bags, items)
            item_to_change = util.get_best_leftover(items)

        util.update_item_list(bags, items)
        print(f"continue: {continue_flag}")
        if continue_flag:
            bags = copy.deepcopy(better_bags)
            items = copy.deepcopy(better_items)
        else:
            local_optima_flag = True
    print("Neighborhood search done.")
    print()
    return best_total_profit
