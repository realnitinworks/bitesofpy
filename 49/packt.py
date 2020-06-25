from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    title = soup.select(".dotd-title")[0].getText().strip()
    description = soup.select(".dotd-main-book-summary div:nth-of-type(3)")[0].getText().strip()
    image = soup.select(".dotd-main-book-image img")[0].attrs['src']
    link = soup.select(".dotd-main-book-image a")[0].attrs['href']

    return Book(title, description, image, link)