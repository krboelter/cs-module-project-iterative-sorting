from iterative_sorting import *

def linear_search(arr, target):
    # Your code here
    for i in arr:
        if target == i:
            return arr.index(i)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    selection_sort(arr)
    start = 0
    end = len(arr) - 1
    answered = False

    while end >= start and not answered:
        middle = start + end // 2

        if target == arr[middle]:
            print(middle)
            print(arr[middle])
            return arr.index(arr[middle])
        elif target > arr[middle]:
            start = middle + 1
            answered = False
        elif target < arr[middle]:
            end = middle - 1
            answered = False
        else:
            answered = True


    return -1  # not found
