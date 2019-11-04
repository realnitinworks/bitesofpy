import csv
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    def difficulty(row):
        return (
            0
            if row['Difficulty'] == 'None'
            else float(row['Difficulty'])
        )

    with open(stats, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=';')
        sorted_bites = sorted(reader, key=difficulty, reverse=True)

    bite_ids = [
        bite['Bite'].split(".")[0][5:]
        for bite in sorted_bites
    ]

    return bite_ids[:N]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
