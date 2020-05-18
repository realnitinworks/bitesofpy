from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_get_sign_with_most_famous_people(signs):
    assert get_sign_with_most_famous_people(signs[:1]) == ("Aries", 32)


signs_compatible = [
    ("Aries", "Leo"),
    ("Aries", "Gemini"),
    ("Leo", "Aries"),
    ("Gemini", "Aries"),
]
@pytest.mark.parametrize('sign1, sign2', signs_compatible)
def test_mutual_compatibility_exit(signs, sign1, sign2):
    assert signs_are_mutually_compatible(signs, sign1, sign2)


signs_inompatibile = [
    ("Aries", "Taurus"),
    ("Taurus", "Aries"),
]
@pytest.mark.parametrize('sign1, sign2', signs_inompatibile)
def test_no_mutual_compatibility(signs, sign1, sign2):
    assert not signs_are_mutually_compatible(signs, sign1, sign2)


dates = [
    (datetime(2012, 1, 20), "Aquarius"),
    (datetime(2012, 1, 30), "Aquarius"),
    (datetime(2012, 2, 18), "Aquarius"),

    (datetime(2012, 2, 19), "Pisces"),
    (datetime(2012, 3, 20), "Pisces"),
    (datetime(2012, 2, 27), "Pisces"),

    (datetime(2012, 3, 21), "Aries"),
    (datetime(2012, 4, 19), "Aries"),
    (datetime(2012, 4, 10), "Aries"),

]
@pytest.mark.parametrize('date, sign', dates)
def test_sign_by_date(signs, date, sign):
    assert get_sign_by_date(signs, date) == sign


def test_signs_type(signs):
    assert all(sign.__class__.__name__ == "Sign" for sign in signs)
