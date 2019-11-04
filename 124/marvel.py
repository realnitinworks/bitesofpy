from collections import Counter, namedtuple
import csv
import re

import requests

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex appearances year')


# csv parsing code provided so this Bite can focus on the parsing

def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode('utf-8')


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])


characters = list(load_data())


# start coding

def most_popular_characters(characters=characters, top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """

    def appearances(character):
        try:
            return int(character.appearances)
        except ValueError:
            return 0

    sorted_characters = sorted(
        characters,
        key=appearances,
        reverse=True
    )

    return [character.name for character in sorted_characters][:top]


def max_and_min_years_new_characters(characters=characters):
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv
       characters, or the 'year' attribute of the namedtuple, return a tuple
       of (max_year, min_year)
    """
    first_appearances_by_year = Counter(
        character.year
        for character in characters
        if character.year
    )

    [(max_year, _)] = first_appearances_by_year.most_common(1)
    min_year, _ = first_appearances_by_year.most_common()[-1]

    return max_year, min_year


def get_percentage_female_characters(characters=characters):
    """Get the percentage of female characters as percentage of all genders
       over all appearances.
       Ignore characters that don't have gender ('sex' attribue) set
       (in your characters data set you should only have Male, Female,
       Agender and Genderfluid Characters.
       Return the result rounded to 2 digits
    """

    def total_appearances(sex=None):
        def condition(character):
            if sex is None:
                return True
            else:
                return character.sex == sex

        return len([
            character
            for character in characters
            if character.sex and condition(character)
        ])

    female_count = total_appearances(sex="Female Characters")

    all_gender_count = total_appearances()

    return round(female_count/all_gender_count*100, 2)
