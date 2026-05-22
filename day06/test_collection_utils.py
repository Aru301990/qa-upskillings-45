from collection_utils import *


def test_sum_array():
    assert sum_array([1, 2, 3]) == 6


def test_find_duplicates():
    assert set(find_duplicates([1, 1, 2])) == {1}


def test_group_words_by_length():

    result = group_words_by_length(["hi", "cat"])

    assert result == {
        2: ["hi"],
        3: ["cat"]
    }


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]