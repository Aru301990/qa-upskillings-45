def sum_array(numbers):
    return sum(numbers)


def find_duplicates(numbers):

    seen = set()
    duplicates = set()

    for num in numbers:

        if num in seen:
            duplicates.add(num)

        seen.add(num)

    return list(duplicates)


def group_words_by_length(words):

    groups = {}

    for word in words:

        length = len(word)

        if length not in groups:
            groups[length] = []

        groups[length].append(word)

    return groups


def sort_by_value(data):

    return sorted(
        data.items(),
        key=lambda item: item[1]
    )


def two_sum(numbers, target):

    seen = {}

    for i, num in enumerate(numbers):

        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return []