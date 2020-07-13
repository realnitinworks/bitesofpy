import datetime
import pytest
from random import randint
from unittest import mock

from tomorrow import tomorrow


def test_no_args():
    fake_today = datetime.date(2020, 7, 9)
    with mock.patch.object(datetime, 'date', mock.Mock(wraps=datetime.date)) as patched:
        patched.today.return_value = fake_today
        assert tomorrow() == datetime.date(2020, 7, 10)


def test_next_day():
    assert tomorrow(datetime.date(2020, 5, 1)) == datetime.date(2020, 5, 2)


def test_next_year():
    assert tomorrow(datetime.date(2019, 12, 31)) == datetime.date(2020, 1, 1)


def test_leap_year():
    assert tomorrow(datetime.date(2020, 2, 28)) == datetime.date(2020, 2, 29)


def test_non_leap_year():
    assert tomorrow(datetime.date(2021, 2, 28)) == datetime.date(2021, 3, 1)


def test_random_date():
    year, month, day = randint(2000, 2020), randint(1, 12), randint(1, 27)
    assert tomorrow(datetime.date(year, month, day)) == datetime.date(year, month, day + 1)