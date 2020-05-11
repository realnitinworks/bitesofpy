import pytest
from unittest.mock import patch


from numbers_to_dec import list_to_decimal


numbers = [
    ([0, 4, 2, 9], 429),
    ([1, 7, 5], 175),
    ([0, 3, 1, 2], 312),
    ([9, 8, 4, 3], 9843)
]


@pytest.mark.parametrize("input, expected", numbers)
def test_valid_values(input, expected):
    actual = list_to_decimal(input)
    assert actual == expected


@pytest.mark.parametrize('input', [
    [6, 2, True],
    [3.6, 4, 1],
    ['4', 5, 3, 1]
])
def test_invalid_input_types(input):
    with pytest.raises(TypeError):
        list_to_decimal(input)


def test_invalid_range():
    input = [10, 2, 3]

    with pytest.raises(ValueError):
        list_to_decimal(input)
