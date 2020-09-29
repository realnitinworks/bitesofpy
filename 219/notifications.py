from datetime import date, timedelta


TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    after = 0
    while True:
        after += num_days
        for _ in range(num_bites):
            yield start_date + timedelta(days=after)
