from datetime import datetime, timedelta
import os
import re
from re import findall
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    timestamp_regex = re.compile(r"\((\d{,2}:\d{,2})\)")
    with open(COURSE_TIMES) as f:
        return timestamp_regex.findall(f.read())


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""

    # Convert timestamps in %M:%S format to datetime objects
    durations = (
        datetime.strptime(timestamp, "%M:%S")
        for timestamp in timestamps
    )

    # Convert datetime objects to timedelta objects
    deltas = (
        timedelta(minutes=timestamp.minute, seconds=timestamp.second)
        for timestamp in durations
    )

    # Sum the deltas
    # total_duration = timedelta()
    # for delta in deltas:
    #     total_duration += delta

    # The above works. But, can I apply sum() method on the timedelta objects?
    # Look at this ticket: https://bugs.python.org/issue25549
    # Need to pass a start value as parameter
    return str(sum(deltas, start=timedelta(0)))
