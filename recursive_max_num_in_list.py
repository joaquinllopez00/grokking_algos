test_arr = [2, 4, 6]


# def max_num_in_list(arr):

#     if len(arr) == 1:
#         return arr[0]
#     else:
#         current_num = arr.pop(0)
#         res_num = max_num_in_list(arr)
#         if current_num > res_num:
#             return current_num
#         else:
#             return res_num


def max_num_in_list(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(max_num_in_list(test_arr))
