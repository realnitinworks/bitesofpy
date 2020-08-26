import string


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [
        word
        for word in text.split()
        if any(letter not in string.printable for letter in word)
    ]
