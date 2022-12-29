test_arr = [2, 4, 6]


# def num_of_items_in_list(arr):
#     total = 0
#     if len(arr) == 1:
#         return 1
#     else:
#         return 1 + num_of_items_in_list(arr[1:])


def num_of_items_in_list(list):
    if list == []:
        return 0
    return 1 + num_of_items_in_list(list[1:])


print(num_of_items_in_list(test_arr))
