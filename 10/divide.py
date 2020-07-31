def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
        if result < 0:
            raise ValueError("numerator or denominator cannot be negative")
        return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise TypeError("numerator and denominator must be int or float")
