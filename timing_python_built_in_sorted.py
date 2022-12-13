import timeit

array = [3, 5, 9, 10, 2]

print(sorted(array))

setup_code = """
array = [3, 5, 9, 10, 2]
sorted_list = []
"""

main_code = """
sorted_list = sorted(array)
"""

def test(array):

    return sorted(array)

print(timeit.timeit(setup = setup_code, stmt = main_code, number = 10))
