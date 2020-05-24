from collections import namedtuple
from itertools import zip_longest


Url = namedtuple('Url', 'protocol domain book dp number query')


def generate_affiliation_link(url):
    url_components = url.split("/")
    url_components = [
        component
        for component in url_components
        if component
    ]
    link = Url(**dict(zip_longest(Url._fields, url_components)))

    return f'http://www.amazon.com/{link.dp}/{link.number}/?tag=pyb0f-20'
