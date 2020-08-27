def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    # count = 0
    # for letter in text:
    #     if letter != ' ':
    #         break
    #     count += 1
    # return count

    return len(text) - len(text.lstrip(" "))
