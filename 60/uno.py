from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()
ZERO_CARD = "0"
REGULAR_CARDS = "1|2|3|4|5|6|7|8|9|Draw Two|Skip|Reverse".split("|")
WILD_CARDS = "Wild|Wild Draw Four".split("|")

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    deck = []
    for suit in SUITS:
        deck.append(UnoCard(suit, ZERO_CARD))
        for _ in range(2):
            for card in REGULAR_CARDS:
                deck.append(UnoCard(suit, card))

    for _ in range(4):
        for card in WILD_CARDS:
            deck.append(UnoCard(None, card))

    return deck
