from dataclasses import dataclass

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    movie_date = parse(movie.release_date)
    actor_date = parse(actor.born)

    actor_age = relativedelta(movie_date, actor_date).years

    return (f"{actor.name} was {actor_age} "
            f"years old when {movie.title} came out.")
