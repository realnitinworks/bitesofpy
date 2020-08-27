from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    aware_dt = naive_utc_dt.replace(tzinfo=utc)
    return aware_dt.astimezone(AUSTRALIA), aware_dt.astimezone(SPAIN)