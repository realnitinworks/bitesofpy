import operator


functions = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """

    operand1, operator, operand2 = calculation.split()

    try:
        operand1 = int(operand1)
        operand2 = int(operand2)
        return functions[operator](operand1, operand2)
    except (KeyError, ZeroDivisionError):
        raise ValueError
