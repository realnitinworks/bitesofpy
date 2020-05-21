import os
import random
import string
import sqlite3

import pytest

from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture(scope="function")
def db():
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)
    m = MovieDb(DB, DATA, TABLE)
    m.init()
    yield m
    m.drop_table()


movies = [
    (1, "The Godfather"),
    (2, "The Shawshank Redemption"),
    (3, "Schindler's List"),
    (4, "Raging Bull"),
    (5, "Casablanca"),
    (6, "Citizen Kane"),
    (7, "Gone with the Wind"),
    (8, "The Wizard of Oz"),
    (9, "One Flew Over the Cuckoo's Nest"),
    (10, "Lawrence of Arabia"),
]
@pytest.mark.parametrize('id, title', movies)
def test_db_initialization(db, id, title):
    db.cur.execute(f"SELECT * from {db.table} WHERE id=?", (f"{id}",))
    row = db.cur.fetchone()
    assert row[1] == title


# write tests for all MovieDb's query / add / delete
def test_add_movie(db):
    last_row_id = db.add('The Big Labowski', 1998, 8.4)
    assert last_row_id == 11

    db.con.row_factory = sqlite3.Row
    db.cur = db.con.cursor()
    db.cur.execute(f"SELECT * from {db.table} WHERE id=?", (last_row_id,))
    row = db.cur.fetchone()

    assert row['id'] == 11
    assert row['title'] == "The Big Labowski"
    assert row['year'] == 1998
    assert row['score'] == 8.4


def test_delete_movie(db):
    db.con.row_factory = sqlite3.Row
    db.cur = db.con.cursor()
    db.cur.execute(f"SELECT * from {db.table} WHERE id=?", (10,))
    row = db.cur.fetchone()
    assert row['id'] == 10

    db.delete(10)
    db.cur.execute(f"SELECT * from {db.table} WHERE id=?", (10,))
    row = db.cur.fetchone()
    assert not row


@pytest.mark.parametrize('title, year, score', DATA)
def test_query_by_title(db,  title, year, score):
    new_title = title.replace("'", "''")  # This had to be done, because of bug in code.
    rows = db.query(title=new_title)
    _, _title, _year, _score = rows[0]
    assert (_title, _year, _score) == (title, year, score)


MOVIES_BY_YEAR = [
    (1972, "The Godfather"),
    (1994, "The Shawshank Redemption"),
    (1993, "Schindler's List"),
    (1980, "Raging Bull"),
    (1942, "Casablanca"),
    (1941, "Citizen Kane"),
    (1939, "Gone with the Wind, The Wizard of Oz"),
    (1975, "One Flew Over the Cuckoo's Nest"),
    (1962, "Lawrence of Arabia"),
]
@pytest.mark.parametrize('year, expected', MOVIES_BY_YEAR)
def test_query_by_year(db, year, expected):
    rows = db.query(year=year)
    titles = ", ".join(row[1] for row in rows)
    assert titles == expected


DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]

MOVIES_BY_SCORE = [
    (9.2, "The Shawshank Redemption"),
    (9.3, ""),
    (8.9, "The Godfather, The Shawshank Redemption"),
    (8.2, "The Godfather, The Shawshank Redemption, "
          "Schindler's List, Casablanca, Citizen Kane, "
          "One Flew Over the Cuckoo's Nest, Lawrence of Arabia"),
]
@pytest.mark.parametrize('score, expected', MOVIES_BY_SCORE)
def test_query_by_score(db, score, expected):
    rows = db.query(score_gt=score)
    titles = ", ".join(row[1] for row in rows)
    assert titles == expected



