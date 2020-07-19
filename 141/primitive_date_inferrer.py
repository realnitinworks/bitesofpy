from enum import Enum
from datetime import datetime
from collections import Counter
from itertools import chain


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt) # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """

    formats = [_maybe_DateFormats(date_str) for date_str in dates]
    # Flattens each item in formats and computes the count of each item
    formats_count = Counter(chain.from_iterable(formats))
    most_common_format, most_common_count = formats_count.most_common(1)[0]
    sorted_format_count_values = sorted(formats_count.values(), reverse=True)

    # Check for tie with another format
    if most_common_count in sorted_format_count_values[1:]:
        raise InfDateFmtError

    # Check for non parsable most common format
    if most_common_format == DateFormat.NONPARSABLE:
        raise InfDateFmtError

    most_common_format_str = DateFormat.get_d_parse_formats(
        most_common_format.value
    )

    result = []
    for date in dates:
        try:
            result.append(
                datetime.strptime(date, most_common_format_str).strftime("%Y-%m-%d")
            )
        except ValueError:
            result.append("Invalid")

    return result
