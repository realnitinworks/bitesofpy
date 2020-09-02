def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """

    sorted_numbers = sorted(enumerate(numbers), key=lambda x: x[1])

    i, j = 0, len(sorted_numbers) - 1

    while i < j:
        sum = sorted_numbers[i][1] + sorted_numbers[j][1]
        indices = sorted_numbers[i][0], sorted_numbers[j][0]

        if sum == target:
            return indices

        if sum < target:
            i += 1
        else:
            j -= 1

    return None
