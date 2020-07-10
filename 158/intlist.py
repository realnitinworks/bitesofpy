import statistics as stat
from decimal import Decimal


class IntList(list):
    def __init__(self, values):
        self.values = values
        super().__init__(values)

    @property
    def mean(self):
        return stat.mean(self.values)

    @property
    def median(self):
        return stat.median(self.values)

    def _validate_and_convert(self, values):
        modified = []
        for value in values:
            if isinstance(value, Decimal):
                value = float(value)
            if type(value) not in {int, float}:
                raise TypeError
            modified.append(value)
        return modified

    def extend(self, values):
        values = self._validate_and_convert(values)
        self.values.extend(values)

    def append(self, values):
        if isinstance(values, list):
            self.extend(values)
        else:
            self.extend([values])

    def __add__(self, other):
        other = self._validate_and_convert(other)
        return self.values + other

    def __iadd__(self, other):
        self.values = self.__add__(other)
        return self.values
