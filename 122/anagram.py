from collections import Counter


def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""

    words = [
        word.replace(" ", "").lower()
        for word in {word1, word2}
    ]

    first, second = words

    return Counter(first) == Counter(second)
