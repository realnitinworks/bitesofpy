from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


hex_colors = [
        (0, 20, 255, "#0014FF"),
        (10, 12, 13, "#0A0C0D"),
        (100, 199, 54, "#64C736"),
        (80, 160, 240, "#50A0F0"),
        (2, 3, 4, "#020304"),
]


@pytest.mark.parametrize('red, blue, green, expected', hex_colors)
@patch('color.sample')
def test_gen_hex_color(mock_sample, gen, red, blue, green, expected):
    mock_sample.return_value = red, blue, green
    assert next(gen) == expected


@patch('color.sample')
def test_sample_range_and_total(mock_sample, gen):
    rgb = 10, 20, 30
    expected = "#0A141E"
    mock_sample.return_value = rgb
    assert next(gen) == expected
    mock_sample.assert_called_with(range(0, 256), 3)
