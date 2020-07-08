class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __len__(self):
        return len(self.values)

    def __matmul__(self, other):
        result = [
            [
                0
                for _ in range(len(other.values[0]))
            ]
            for _ in range(len(self))
        ]

        # Iterate through rows of self
        for i in range(len(self)):
            # Iterate through columns of other
            for j in range(len(other.values[0])):
                # Iterate through rows of other
                for k in range(len(other.values)):
                    result[i][j] += self.values[i][k] * other.values[k][j]

        return Matrix(result)

    def __rmatmul__(self, other):
        return self @ other

    def __imatmul__(self, other):
        self.values = (self @ other).values
        return self
