def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2  # total length of the list
        guess = list[mid]  # guess the item in the middle of the list
        if guess == item:
            return mid  # if our guess (mid) is equal to item, return the mid index
        if (
            guess > item
        ):  # if our guess was greater than the item, then set current mid to new high
            high = mid - 1
        else:  # if our guess was lower than the item, then set current mid to the low
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None
