from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')
ONE_MIN_EARTH = 60  # seconds
ONE_HOUR_EARTH = ONE_MIN_EARTH * 60  # seconds
ONE_HOUR_MILLER = 7 * 365 * 24  # earth days
ONE_MIN_MILLER = ONE_HOUR_MILLER * 60  # earth minutes


def _remaining(start_date, converter=ONE_HOUR_EARTH, rounded=2):
    return round(
        (PY2_DEATH_DT - start_date).total_seconds() / converter,
        ndigits=rounded
    )


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    return _remaining(start_date)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    return _remaining(start_date, converter=ONE_MIN_MILLER)
