test_arr = [2, 4, 6]
# def sum(arr):
#     total = 0
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         total = arr.pop(0)
#         return total + sum(arr)


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(sum(test_arr))  # => 12
