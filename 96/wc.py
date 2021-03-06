def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    n_lines = 0
    n_words = 0
    n_chars = 0

    with open(file_) as f:
        for line in f:
            n_lines += 1
            n_words += len(line.split())
            n_chars += len(line)

    return f"{n_lines}  {n_words}  {n_chars}  {file_}"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
