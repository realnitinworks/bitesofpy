import string


ALPHANUM = string.ascii_letters + string.digits


def get_index_different_char(chars):
    alphanumeric = [
        letter for letter in chars
        if str(letter) and str(letter) in ALPHANUM
    ]

    non_alphanumeric = [
        letter for letter in chars
        if str(letter) and str(letter) not in ALPHANUM
    ]

    char_index = {
        value: key
        for key, value in enumerate(chars)
    }

    different_char = (
        alphanumeric[0]
        if len(alphanumeric) == 1  # Always 1 diff char
        else non_alphanumeric[0]
    )

    return char_index[different_char]
