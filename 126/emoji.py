import sys
import unicodedata


START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji, '')
    except TypeError:
        return 'Not found'


def _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    return {
        chr(n): what_means_emoji(chr(n))
        for n in range(START_EMOJI_RANGE, sys.maxunicode + 1)
    }


def find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""

    emoji_mapping = _make_emoji_mapping()
    max_length = max(len(value) for value in emoji_mapping.values())
    for emoji, name in emoji_mapping.items():
        if term.lower() in name.lower():
            print(f"{name:<{max_length}} | {emoji}")
