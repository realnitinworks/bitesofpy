import datetime


def tomorrow(today=None):
    if not today:
        today = datetime.date.today()
    return today + datetime.timedelta(days=1)
