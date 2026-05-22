# string_utils.py


def reverse_string(text):
    return text[::-1]


def count_vowels(text):

    vowels = "aeiouAEIOU"

    count = 0

    for char in text:

        if char in vowels:
            count += 1

    return count


def check_anagram(str1, str2):

    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    return str1 == str2


def capitalize_words(text):

    words = text.split()

    capitalized = []

    for word in words:
        capitalized.append(word.capitalize())

    return " ".join(capitalized)


def character_frequency(text):

    freq = {}

    for char in text:

        freq[char] = freq.get(char, 0) + 1

    return freq