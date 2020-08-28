from decimal import Decimal, ROUND_HALF_EVEN


def round_even(number):
    """Takes a number and returns it rounded even"""
    return Decimal(number).to_integral_value(ROUND_HALF_EVEN)
