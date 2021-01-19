import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    args = (arg for arg in args if arg)
    try:
        result = set(next(args))
    except StopIteration:
        return set()

    result = result.intersection(*args)
    return result

