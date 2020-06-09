import unicodedata


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    yield from (c.lower() for c in text if 'WITH' in unicodedata.name(c))
