from collections import Counter


VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    vowels_count = Counter()

    for word in text.lower().split():
        if word in vowels_count:
            continue

        for c in word:
            if c in VOWELS:
                vowels_count[word] += 1

    return vowels_count.most_common(1)[0]
