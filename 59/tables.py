class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.x, self.y = length, length
        self._table = []

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self.x * self.y

    def __str__(self):
        """Returns a string representation of the table"""
        table = []
        for x in range(1, self.x + 1):
            results = " | ".join(str(x * y) for y in range(1, self.y + 1))
            table.append(results)
        return "\n".join(table)

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if x > self.x or y > self.y:
            raise IndexError
        return x * y
