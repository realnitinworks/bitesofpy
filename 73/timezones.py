import pytz
from pytz import timezone


MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""

    aware_dt = utc.replace(tzinfo=pytz.utc)
    try:
        return all(
            aware_dt.astimezone(timezone(zone)).hour in MEETING_HOURS
            for zone in timezones
        )
    except pytz.exceptions.UnknownTimeZoneError as e:
        raise ValueError(f"Wrong/Unknown Timezone: {e}")
