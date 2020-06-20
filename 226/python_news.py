from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    titles = (
        title.getText().strip()
        for title in soup.select(".title")
    )

    comments = (
        int(comment.getText().split()[0])
        for comment in soup.select(".naturaltime a")
    )

    points = (
        int(point.getText().split()[0])
        for point in soup.select(".controls .smaller")
    )

    entries = (
        Entry(title=title, points=points, comments=comments)
        for title, points, comments in zip(titles, points, comments)
    )

    def points_comments_key(entry):
        return entry.points, entry.comments  # Tuple comparison 15, 0 > 9, 4

    return sorted(entries, key=points_comments_key, reverse=True)[:top]