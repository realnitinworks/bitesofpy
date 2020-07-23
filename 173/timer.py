from datetime import datetime
import re
from dateutil.relativedelta import relativedelta

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    days_regex = re.compile(r"(\d+)d")
    hours_regex = re.compile(r"(\d+)h")
    minutes_regex = re.compile(r"(\d+)m")
    seconds_regex = re.compile(r"(\d+)s")

    days = days_regex.findall(delay_time)
    hours = hours_regex.findall(delay_time)
    minutes = minutes_regex.findall(delay_time)
    seconds = seconds_regex.findall(delay_time)

    days = int(days[0]) if days else 0
    hours = int(hours[0]) if hours else 0
    minutes = int(minutes[0]) if minutes else 0
    seconds = int(seconds[0]) if seconds else 0

    if all(not item for item in {days, hours, minutes, seconds}):
        seconds = int(delay_time)  # no units eg: 45 for 45s

    future_time = (
        start_time +
        relativedelta(
            days=+days,
            hours=+hours,
            minutes=+minutes,
            seconds=+seconds
        )
    )
    return f"{task} @ {future_time}"
