from string_utils import *


def test_reverse_string():
    assert reverse_string("abc") == "cba"


def test_count_vowels():
    assert count_vowels("hello") == 2


def test_check_anagram():
    assert check_anagram("listen", "silent") == True


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_character_frequency():
    assert character_frequency("aa") == {"a": 2}