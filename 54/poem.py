import textwrap

INDENTS = 4


def print_hanging_indents(poem):
    indent = True
    formatted_poem = []

    for line in poem.split("\n"):
        if not line:  # indication that next line is a new block
            indent = False  # Turn off indentation for the first line of new block
            continue  # ignore the blank lines

        if not indent:
            formatted_line = textwrap.dedent(line)  # dedent the first line in the block
            indent = True  # indent the rest of the lines in the block
        else:
            formatted_line = textwrap.indent(line.strip(), prefix=" " * INDENTS)            

        formatted_poem.append(formatted_line)

    print("\n".join(formatted_poem))
