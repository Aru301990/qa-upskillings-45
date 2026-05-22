from collection_utils import sum_array
from collection_utils import find_duplicates
from collection_utils import group_words_by_length
from collection_utils import sort_by_value
from collection_utils import two_sum


# Sum Array
numbers = [10, 20, 30, 40]

print("Sum Array:")
print(sum_array(numbers))


# Find Duplicates
numbers = [1, 2, 3, 2, 4, 1]

print("\nFind Duplicates:")
print(find_duplicates(numbers))


# Group Words By Length
words = ["hi", "python", "cat", "automation"]

print("\nGroup Words By Length:")
print(group_words_by_length(words))


# Sort Dictionary By Value
scores = {
    "A": 80,
    "B": 95,
    "C": 70
}

print("\nSort By Value:")
print(sort_by_value(scores))


# Two Sum
numbers = [2, 7, 11, 15]

target = 9

print("\nTwo Sum:")
print(two_sum(numbers, target))