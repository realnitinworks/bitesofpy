from datetime import datetime, timedelta


PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    count_100, count_year = 1, 1

    while True:
        if count_100 % 4 == 0:
            yield PYBITES_BORN + count_year * timedelta(days=365)
            count_year += 1
        yield PYBITES_BORN + count_100 * timedelta(days=100)
        count_100 += 1
