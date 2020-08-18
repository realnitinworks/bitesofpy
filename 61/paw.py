from collections import namedtuple
import random
import string
from itertools import product

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')


def create_paw_deck(n=8):
    if n > 26:
        raise ValueError

    alphabets = string.ascii_uppercase[:n]

    cards = [
        "".join(str(it) for it in item)
        for item in product(alphabets, NUMBERS)
    ]

    random_cards = [
        random.choice([
            card
            for card in cards 
            if card.startswith(alphabet)
        ])
        for alphabet in alphabets
    ]

    other_cards = [
        card
        for card in cards
        if card not in random_cards
    ]

    return [
        PawCard(card, random.choice(ACTIONS))
        for card in random_cards
    ] + [
        PawCard(card, None)
        for card in other_cards
    ]
