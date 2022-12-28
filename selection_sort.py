def findSmallest(arr):
    smallest = arr[0]  # set smallest to first idx of arr initially
    smallest_index = 0  # set idx to 0
    for i in range(1, len(arr)):  # loop through the arr
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(1, len(arr)):  # loops through array
        smallest = findSmallest(
            arr
        )  # uses helper function to find the smallest element of array
        newArr.append(
            arr.pop(smallest)
        )  # pops the smallest index, adding it the the new array
    return newArr  # returns the newArr


print(
    selectionSort([5, 3, 2, 109, 7, 9, 3, 6, 11, 222, 9])
)  # => [2, 3, 3, 5, 6, 7, 9, 9, 11, 109]
