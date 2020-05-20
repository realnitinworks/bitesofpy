from unittest.mock import patch

import pytest

from guess import GuessGame, InvalidNumber


# write test code to reach 100% coverage and a 100% mutpy 
invalid_numbers = [
    ("invalid", "Not a number"),
    ("-10", "Negative number"),
    (-4, "Negative number"),
    (16, "Number too high")
]
@pytest.mark.parametrize('secret_number, exception_value', invalid_numbers)
def test_non_integer_secret_number(secret_number, exception_value):
    with pytest.raises(InvalidNumber, match=exception_value):
        GuessGame(secret_number)


def test_game_initialization():
    g = GuessGame(10)
    assert g.secret_number == 10
    assert g.max_guesses == 5
    assert g.attempt == 0

    g = GuessGame(15, 20)
    assert g.secret_number == 15
    assert g.max_guesses == 20
    assert g.attempt == 0

    g = GuessGame(0, 20)
    assert g.secret_number == 0
    assert g.max_guesses == 20
    assert g.attempt == 0


@patch('guess.input')
def test_correct_guess(mock_input, capfd):
    g = GuessGame(5, max_guesses=1)
    mock_input.return_value = 5
    g()
    assert g.attempt == 1
    captured = capfd.readouterr()
    assert captured.out == "Guess a number: \nYou guessed it!\n"


@patch('guess.input')
def test_guess_too_low(mock_input, capfd):
    g = GuessGame(5, max_guesses=1)
    mock_input.return_value = 1
    g()
    captured = capfd.readouterr()
    assert captured.out == "Guess a number: \nToo low\nSorry, the number was 5\n"


@patch('guess.input')
def test_guess_too_high(mock_input, capfd):
    g = GuessGame(5, max_guesses=1)
    mock_input.return_value = 10
    g()
    captured = capfd.readouterr()
    assert captured.out == "Guess a number: \nToo high\nSorry, the number was 5\n"


@patch('guess.input')
def test_invalid_input(mock_input, capfd):
    g = GuessGame(5, max_guesses=10)
    mock_input.side_effect = ['invalid', 5]
    g()
    captured = capfd.readouterr()
    assert captured.out == (
        "Guess a number: \n"
        "Enter a number, try again\n"
        "Guess a number: \n"
        "You guessed it!\n"
    )