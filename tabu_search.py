from typing import List, Tuple
import util
import random
import copy


def tabu_search(data: Tuple[List[int], List[int], List[int]], tabu_list_length=10, tabu_max_iter=50):

    tabu_list: List[int] = []
    tabu_iter = 0

    (items, bags) = util.process_data(data)

    items.sort(key=lambda x: x.benefit, reverse=True)
    bags.sort(key=lambda x: x.capacity, reverse=False)

    original_bags = copy.deepcopy(bags)
    original_items = copy.deepcopy(items)

    best_solution: List[int] = []
    best_total_profit = 0

    second_solution: List[int] = []
    second_total_profit = 0

    # Get the first solution with greedy search
    for item in items:
        for bag in bags:
            if bag.capacity_left >= item.weight:
                bag.add_item(item)
                break

    # tabu_list.append(copy.deepcopy(best_total_profit))

    # print(best_solution)
    # print(best_total_profit)


    # Tabu search
    iter_flag = True
    while iter_flag:

        best_solution = []
        best_total_profit = 0
        best_bags = copy.deepcopy(original_bags)
        best_items = copy.deepcopy(original_items)

        item_to_change = util.get_best_leftover(items)
        # item_to_change = util.get_random_leftover(items)

        if item_to_change == None:
            print("No item leftover. Best solution has been found.")
            # print(f"solution: {best_solution}")
            # print(f"profit: {best_total_profit}")
            return best_total_profit

        # random.shuffle(bags)

        last_bags = copy.deepcopy(bags)
        last_items = copy.deepcopy(items)
        util.update_item_list(bags, items)

        for k in range(len(bags)):
            rotate = False
            for i in range(len(bags)):
                util.update_item_list(bags, items)
                bag = bags[i]
                next_bag = bags[i + k - len(bags) if i + 1 + k >= len(bags) else i + 1 + k]

                f = False       

                # Select two items in two bags to rotate
                for item_1 in bag.items:
                    if f:
                        break
                    for item_2 in next_bag.items:
                        if f:
                            break
                        if bag.capacity_left + item_1.weight >= item_to_change.weight \
                            and next_bag.capacity_left + item_2.weight >= item_1.weight:
                            rotate = True
                            f = True
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
                            util.update_item_list(bags, items)
                            break
            
            util.update_item_list(bags, items)
            current_solution = [item.bag for item in items]
            current_total_profit = util.get_total_profit_of_bags(bags)
            print(f"i: {k}", end=" ")
            print(f"rotate: {rotate}", end=" ")
            print(f"current_total_profit: {current_total_profit}")
            # print(f"bags: {bags}")

            if current_total_profit > best_total_profit and not util.is_in_tabu_list(tabu_list, current_total_profit):

                best_total_profit = current_total_profit
                best_solution = current_solution
                best_bags = copy.deepcopy(bags)
                best_items = copy.deepcopy(items)

                print(f"update best_total_profit: {best_total_profit}")

            bags = copy.deepcopy(last_bags)
            items = copy.deepcopy(last_items)
            util.update_item_list(bags, items)
            item_to_change = util.get_best_leftover(items)
        
        bags = copy.deepcopy(best_bags)
        items = copy.deepcopy(best_items)
        util.update_item_list(bags, items)
        item_to_change = util.get_best_leftover(items)

        if best_total_profit != 0 and not util.is_in_tabu_list(tabu_list, best_total_profit):
            tabu_list.append(copy.deepcopy(best_total_profit))
            print(f"update tabu list: {tabu_list}")

        if len(tabu_list) > tabu_list_length:
            tabu_list.pop(0)

        tabu_iter += 1
        if tabu_iter == tabu_max_iter or best_total_profit == 0:
            print(f"Final Tabu list: {tabu_list}")
            print("Tabu search done.")
            print()
            iter_flag = False

    return util.get_best_in_tabu_list(tabu_list)
