from pprint import PrettyPrinter
from typing import Any


def pretty_string(obj: Any) -> str:
    p = PrettyPrinter(width=60, depth=2, sort_dicts=True)
    return p.pformat(obj)