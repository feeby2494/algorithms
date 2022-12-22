# Only works on already sorted data

# Iterative Binary Search

from unittest import result


def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            start = mid - 1
        else:
            return mid
        
    return start
    #return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 10

result = binary_itr(arr, 0, len(arr) - 1, target)

print (result)