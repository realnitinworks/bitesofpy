def countdown():
    """Write a generator that counts from 100 to 1"""
    yield from range(100, 0, -1)
