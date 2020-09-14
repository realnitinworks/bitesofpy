WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""

    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print(WHITE, end="")
            else:
                print(BLACK, end="")
        print()  # newline
