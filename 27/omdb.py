import glob
import json
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movie_data = []
    for file in files:
        with open(file) as f:
            movie_data.append(json.load(f))
    return movie_data


def get_single_comedy(movies):
    movies = [
        movie['Title']
        for movie in movies
        if 'Comedy' in movie['Genre']
    ]

    return movies and movies[0]


def get_movie_most_nominations(movies):
    movies_by_nominations = (
        (movie['Title'], int(movie['Awards'].split('&')[1].strip().split()[0]))
        for movie in movies
    )

    movie, _ = max(movies_by_nominations, key=lambda x: x[1])
    return movie


def get_movie_longest_runtime(movies):
    movies_by_runtime = (
        (movie['Title'], int(movie['Runtime'].split()[0]))
        for movie in movies
    )

    movie, _ = max(movies_by_runtime, key=lambda x: x[1])
    return movie