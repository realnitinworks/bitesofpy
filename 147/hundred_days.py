from datetime import date

from dateutil.rrule import MO, TU, WE, TH, FR, WEEKLY, rrule

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    dates = rrule(
        WEEKLY,
        count=100,
        byweekday=(MO, TU, WE, TH, FR),
        dtstart=start_date
    )

    return [
        date(dt.year, dt.month, dt.day)
        for dt in dates
    ]
