def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""

    # langs_iterator = iter(programmers.values())
    # common_languages = set(next(langs_iterator))  # Initialize with a value

    # for langs in langs_iterator:   # Loop over the next values
    #     common_languages &= set(langs)  # set operation on the values

    # return common_languages

    return set.intersection(*(set(langs) for langs in programmers.values()))
