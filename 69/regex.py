import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    timestamp_regex = re.compile(r'\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d')
    return timestamp_regex.search(text) is not None


def is_integer(number):
    """Return True if number is an integer"""
    integer_regex = re.compile(r'^-?\d+$')
    return integer_regex.search(str(number)) is not None


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    word_with_dash_regex = re.compile(r'\w+-\w+')
    return word_with_dash_regex.search(text) is not None


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    word_in_parenthesis_regex = re.compile(r'\s\(\S+\)')
    return word_in_parenthesis_regex.sub("", text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    string_regex = re.compile(r"[^?!.,;]+")
    strings = [
        string.strip()
        for string in string_regex.findall(text)
    ]

    # using finditer
    # strings = [
    #     mo.group().strip()
    #     for mo in string_regex.finditer(text)
    # ]

    return strings


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    space_regex = re.compile(r'\s+')
    return space_regex.sub(" ", text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    vowel_regex = re.compile(r'[aeiou]{3,}')
    return vowel_regex.search(word) is not None


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    emea_regex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    return emea_regex.sub(r"\2/\1/\3", date)
