from collections import Counter


def freq_digit(num: int) -> int:
    num_string = str(num)
    digit_frequency = Counter(num_string)
    most_frequent_digit, frequency = digit_frequency.most_common()[0]
    return int(most_frequent_digit)
