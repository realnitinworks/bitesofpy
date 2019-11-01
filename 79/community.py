import csv

import requests
from collections import Counter

CSV_URL = 'https://bit.ly/2HiD2i8'
PLUS = '+'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded = download.content.decode('utf-8')

    reader = csv.DictReader(decoded.splitlines())
    return (
        row['tz']
        for row in reader
    )


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    bar_chart_data = Counter(content)
    max_len_tz = len(max(bar_chart_data, key=len))

    for tz, count in sorted(bar_chart_data.items()):
        print(f'{tz:<{max_len_tz}} | {PLUS * count}')
