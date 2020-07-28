from datetime import date
from dateutil.relativedelta import relativedelta, SU

JANUARY = 1
FIRST_JANUARY = 1
JANUARY_TO_MAY = 4
SECOND = 2


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""

    dt = date(year=year, month=JANUARY, day=FIRST_JANUARY)
    return dt + relativedelta(months=+JANUARY_TO_MAY, weekday=SU(+SECOND))
