import os
import urllib.request
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'
SENDING_TO_SLACK = "sending to slack"
PYTHON = "Python"

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    safari_stats = defaultdict(str)

    with open(SAFARI_LOGS) as f:
        while True:
            try:
                first, second = next(f), next(f)
                if SENDING_TO_SLACK not in second:
                    continue

                month_day, *_ = second.split()
                safari_stats[month_day] += PY_BOOK if PYTHON in first else OTHER_BOOK
            except StopIteration:
                break

    for month_day, stat in safari_stats.items():
        print(f"{month_day} {stat}")
