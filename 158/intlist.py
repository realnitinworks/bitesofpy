import statistics as stat


class IntList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def mean(self):
        return stat.mean(self)

    @property
    def median(self):
        return stat.median(self)

    def _validate_int(self, values):
        try:
            return [int(value) for value in values]
        except ValueError:
            raise TypeError

    def extend(self, values):
        values = self._validate_int(values)
        super().extend(values)

    def append(self, values):
        if isinstance(values, list):
            self.extend(values)
        else:
            self.extend([values])

    def __add__(self, other):
        values = self._validate_int(other)
        return super().__add__(values)

    def __iadd__(self, other):
        # Delegating to this class's __add__ method
        self = self.__add__(other)
        return self

        # The following also works
        # Delegating to list's __iadd__ method
        # values = self._validate_int(other)
        # return super().__iadd__(values)
