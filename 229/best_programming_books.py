from pathlib import Path
from urllib.request import urlretrieve
from operator import attrgetter

from bs4 import BeautifulSoup

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    def __init__(self, title, author, year, rank, rating):
        self.title = title
        self.author = author
        self.year = year
        self.rank = rank
        self.rating = rating

    @property
    def last_name(self):
        return self.author.split(",")[0]

    @property
    def title_lower_case(self):
        return self.title.lower()

    def __str__(self):
        return (f"[{str(self.rank).zfill(3)}] {self.title} ({self.year})"
                f"\n      {self.author} {float(self.rating)}")


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    if year:
        books = [
            book
            for book in books
            if book.year >= year
        ]

    for book in books[:limit]:
        print(book)


def names(author):
    """
    Extract first_name, last_name from the given name
    """
    name = author.split()
    last_name = name[-1]
    first_name = " ".join(name[:-1])
    return first_name, last_name


def format_author(first_name, last_name):
    """ Format the author name """
    return f"{last_name}, {first_name}"


def multi_sort(data, specs):
    """
    Wrapper function that can take a list and
    tuples of field and order to sort them on multiple passes.
    https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
    """

    for key, reverse in reversed(specs):
        data.sort(key=attrgetter(key), reverse=reverse)


def extract_data(soup, pattern="python"):
    """
    Extract the info required from soup object
    to create the Book class objects
    """
    for book in soup.select('.book'):
        try:
            title = book.select_one('.book-header .book-title h2').get_text()
            if pattern.lower() not in title.lower():
                continue
            rank = int(book.select_one('.rank').get_text())
            author = book.select_one('.book-header .authors a').get_text()
            first_name, last_name = names(author)
            author = format_author(first_name, last_name)
            year = int(book.select_one('.book-header .date').get_text().strip("| "))
            rating = float(book.select_one('.book-header .our-rating').get_text())
        except AttributeError:
            continue

        yield Book(title, author, year, rank, rating)


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    soup = _get_soup(html_file)

    # extract the info required to create Book class objects
    python_books = list(extract_data(soup))

    # Sort order: List of ('criteria', asc/desc order) tuples
    specs = [
        ('rating', True),
        ('year', False),
        ('title_lower_case', False),
        ('last_name', False)
    ]

    # Inplace sort based on sort order
    multi_sort(python_books, specs)

    # Update the rank after sorting
    for rank, book in enumerate(python_books, start=1):
        book.rank = rank

    return python_books


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""