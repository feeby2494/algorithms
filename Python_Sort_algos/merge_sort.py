from merge import merge
from run_sorting_algorithm.run_sorting_algorithm import run_sorting_algorithm
from random import randint

def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

if __name__ == "__main__":
    ARRAY_LENGTH = 10000
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999

    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="merge_sort", array=array)
