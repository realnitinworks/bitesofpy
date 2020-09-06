from itertools import chain


STAR = '*'


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    rhombus = [
        range(1, width + 1, 2),  # Upper part of rhombus
        range(width - 2, 0, -2)  # Lower part of rhombus
    ]

    for n in chain.from_iterable(rhombus):
        yield f"{STAR * n:^{width}}"  # :^ => aligns center
