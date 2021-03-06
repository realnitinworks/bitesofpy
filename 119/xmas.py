def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    tree = []
    n_spaces = rows - 1

    for row in range(1, rows + 1):
        n_stars = 2 * row - 1
        stars = '*' * n_stars
        align = n_stars + n_spaces
        tree.append(f"{stars:>{align}}")
        n_spaces -= 1

    return "\n".join(tree)
