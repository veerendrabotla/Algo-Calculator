import random

def randomized_quick_sort(arr):
    """Randomized Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    return randomized_quick_sort(less_than_pivot) + equal_to_pivot + randomized_quick_sort(greater_than_pivot)

def random_sampling(data, sample_size):
    """Randomly samples a subset of data."""
    return random.sample(data, sample_size)