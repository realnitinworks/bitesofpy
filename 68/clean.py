import string


def remove_punctuation(input_string: str):
    """Return a str with punctuation chars stripped out"""
    # formatted_string = [
    #     c
    #     for c in input_string
    #     if c not in string.punctuation
    # ]

    # return "".join(formatted_string)

    mapping = {ord(c): None for c in string.punctuation}

    return input_string.translate(mapping)
