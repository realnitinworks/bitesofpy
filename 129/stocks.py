from collections import defaultdict

import requests
from collections import Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0

    new_cap = cap[1:-1]

    if cap[-1] == 'M':
        return float(new_cap)

    if cap[-1] == 'B':
        return float(new_cap) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""

    all_cap_sum = sum(
        _cap_str_to_mln_float(stock['cap'])
        for stock in data
        if stock['industry'] == industry
    )

    return round(all_cap_sum, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    stock_with_highest_cap = max(
        data,
        key=lambda stock: _cap_str_to_mln_float(stock['cap'])
    )

    return stock_with_highest_cap['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sectors_by_stocks = Counter(
        stock['sector']
        for stock in data
        if stock['sector'] != 'n/a'
    )

    sector_with_most_stocks, _ = sectors_by_stocks.most_common()[0]
    sector_with_least_stocks, _ = sectors_by_stocks.most_common()[-1]

    return sector_with_most_stocks, sector_with_least_stocks
