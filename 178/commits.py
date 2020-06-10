from collections import Counter
import os
import re
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """

    number_regex = re.compile(r"\d+")
    commits_amount = Counter()

    with open("/tmp/commits") as f:
        for line in f:
            date_str, history_str = line.split("|")
            if year and str(year) not in date_str:  # Filter based on year
                continue
            year_month = parse(date_str, fuzzy=True).strftime("%Y-%m") 
            total_modifications = sum(
                int(number)
                for number in number_regex.findall(history_str)[1:]  # Ignore the number of file changes
            )
            commits_amount[year_month] += total_modifications

    most_active_month, _ = commits_amount.most_common()[0]
    least_active_month, _ = commits_amount.most_common()[-1]
    return least_active_month, most_active_month
