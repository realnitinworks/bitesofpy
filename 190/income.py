import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from urllib.request import urlretrieve

# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def _get_root(xml):
    return ET.parse(xml).getroot()


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    income_distribution = defaultdict(list)
    root = _get_root(xml)

    for country in root:
        income_level = country[4].text
        country_name = country[1].text
        income_distribution[income_level].append(country_name)

    return dict(income_distribution)
