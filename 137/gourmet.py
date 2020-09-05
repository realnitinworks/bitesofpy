#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter, defaultdict
from itertools import product
import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


WINES = {
    "all": RED_WINES + WHITE_WINES + SPARKLING_WINES,
    "white": WHITE_WINES,
    "red": RED_WINES,
    "sparkling": SPARKLING_WINES,
}


def similarity_score(wine, cheese):
    wine_counter = Counter(wine.lower())
    cheese_counter = Counter(cheese.lower())

    wine_cheese_intersection = set(wine_counter).intersection(cheese_counter)
    final = {
            char: (
                wine_counter[char]
                if wine_counter[char] <= cheese_counter[char]
                else cheese_counter[char]
            )
            for char in wine_cheese_intersection
    }

    score = sum(final.values()) / (1 + (len(wine) - len(cheese)) ** 2)

    return score


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    try:
        wines = WINES[wine_type]
    except KeyError:
        raise ValueError(f"'{wine_type}' is not a valid wine type")

    scores = (
        (wine, cheese, similarity_score(wine, cheese))
        for wine, cheese in product(wines, CHEESES)
    )

    return max(scores, key=operator.itemgetter(2))  # key - based on score


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    wines = WINES["all"]
    wine_cheeses = defaultdict(list)

    for wine, cheese in product(wines, CHEESES):
        wine_cheeses[wine].append(cheese)

    for wine in wine_cheeses:
        wine_cheeses[wine] = sorted(
            wine_cheeses[wine],
            key=lambda cheese: (-similarity_score(wine, cheese), cheese),
        )[:5]

    return sorted(wine_cheeses.items(), key=operator.itemgetter(0))  # wine name
