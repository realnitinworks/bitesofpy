import textwrap
from itertools import zip_longest


COL_WIDTH = 20


def text_to_columns(text):
    # gen_exp
    # split text by paragraphs(\n\n)
    # then split each paragraph to columns (.wrap)
    content = (
       textwrap.wrap(paragraph, width=COL_WIDTH)
       for paragraph in text.split("\n\n")
    )

    # zip together columns
    pre_formatted = zip_longest(*content, fillvalue='')

    # double join
    # first join : add space between columns
    # second join: add newline after a row
    return "\n".join("    ".join(line) for line in pre_formatted)
