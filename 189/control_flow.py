import string


IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    count = 0
    found_digit = False
    for name in names:
        if name.startswith(IGNORE_CHAR):
            continue

        for char in name:
            if char.isdigit():
                found_digit = True
                break

        if found_digit:
            found_digit = False
            continue

        if name.startswith(QUIT_CHAR):
            break
        
        count += 1
        if count > MAX_NAMES:
            break

        yield name
