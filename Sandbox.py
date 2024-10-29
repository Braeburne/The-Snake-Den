import timeit

# Measure execution time of binary_search
setup = '''
import random
import math

def binary_search(array, target, start_index, end_index):
    if start_index > end_index:
        return "binary search not valid"
    middle = math.floor((start_index + end_index) / 2)
    if array[middle] == target:
        return f"Target found at index {middle}"
    if array[middle] > target:
        return binary_search(array, target, start_index, middle - 1)
    if array[middle] < target:
        return binary_search(array, target, middle + 1, end_index)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = random.randint(1, 10)
'''

stmt = 'binary_search(arr, target, 0, len(arr) - 1)'
print(timeit.timeit(stmt, setup=setup, number=1000))
