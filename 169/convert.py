import operator

ALLOWED_TYPES = {int, float}
ALLOWED_FORMATS = {"in", "cm"}
DECIMAL_PLACES = 4
CONVERTER = 2.54


def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """

    if not any(isinstance(value, t) for t in ALLOWED_TYPES):
        raise TypeError(f"value type must be one of {ALLOWED_TYPES}")

    if fmt.lower() not in ALLOWED_FORMATS:
        raise ValueError(f"fmt must be one of {ALLOWED_FORMATS}")

    oper = operator.mul if fmt.lower() == "cm" else operator.truediv
    return round(oper(value, CONVERTER), DECIMAL_PLACES)
