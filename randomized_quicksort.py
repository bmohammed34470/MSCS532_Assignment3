import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Choose pivot uniformly at random
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = randomized_quicksort(arr)
print("Sorted array:", sorted_arr)