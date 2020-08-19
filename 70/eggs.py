from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit):
        self.limit = limit
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.limit:
            self.index += 1
            return f"{choice(COLORS)} egg"
        raise StopIteration
