from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)
TABLE_DATA_START = 4
TABLE_DATA_END = 2
DATE_COLUMN = 1


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    lines = data.splitlines()
    lines = lines[
        TABLE_DATA_START:-TABLE_DATA_END
    ]  # Leave out the table header and the table boundaries
    dates = {line.split("|")[DATE_COLUMN].strip() for line in lines}
    dates = {date.fromisoformat(d) for d in dates}

    return dates


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    streak = 0
    monitor_date = TODAY
    delta = timedelta(days=1)
    yesterday = TODAY - delta

    for d in sorted(dates, reverse=True):
        if d != monitor_date and d != yesterday:
            break

        streak += 1
        monitor_date = d - delta

    return streak
