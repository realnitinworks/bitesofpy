from dateutil.parser import parse


MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    reboot_dates = [
        parse(line, fuzzy=True)
        for line in reboots.strip().splitlines()
    ]

    # iterable of tuples: each tuple -- (days_difference, date_str)
    uptime_diffs = (
        ((dt1 - dt2).days, dt1.date().strftime("%Y-%m-%d"))
        for dt1, dt2 in zip(reboot_dates, reboot_dates[1:])
    )

    # Return the tuple with the highest days_difference
    return max(uptime_diffs, key=lambda x: x[0])
