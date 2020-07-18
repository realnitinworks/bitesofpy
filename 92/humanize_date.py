from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""

    try:
        offset = (NOW - date) / timedelta(seconds=1)
    except TypeError:
        raise ValueError(f"Invalid input date: {date}")

    if offset < 0:
        raise ValueError(f"Input date: {date} cannot be in the future.")

    for time_offset in TIME_OFFSETS:
        if offset < time_offset.offset:
            divider = time_offset.divider
            if divider:
                offset = offset / divider
            offset = int(offset)
            return time_offset.date_str.format(offset)
    return date.strftime("%m/%d/%y")
