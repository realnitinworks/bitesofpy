from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence = "".join(
        character
        for character in sequence
        if character not in {" ", "\n", ".", "!", "?", "/", ","}
    )

    sequence_count = Counter(base.lower() for base in sequence)

    gc_count = sum(
        count
        for base, count in sequence_count.items()
        if base in {"g", "c"}
    )

    all_count = sum(sequence_count.values())

    return round(gc_count/all_count * 100, 2)
