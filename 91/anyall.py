import string


VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(letter.lower() in VOWELS for letter in input_str)


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any(letter.lower() in PYTHON for letter in input_str)


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return any(letter in string.digits for letter in input_str)
