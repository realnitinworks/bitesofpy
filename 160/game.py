import csv
import os
from urllib.request import urlretrieve
from collections import defaultdict

BATTLE_DATA = os.path.join('/tmp', 'battle-table.csv')
if not os.path.isfile(BATTLE_DATA):
    urlretrieve('https://bit.ly/2U3oHft', BATTLE_DATA)


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_mapping = defaultdict(set)
    with open(BATTLE_DATA) as f:
        reader = csv.DictReader(f)
        return {
            row['Attacker']: set(
                opponent
                for opponent, status in row.items()
                if status == 'win'
            )
            for row in reader
        }


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()

    if player1 == player2:
        return "Tie"

    for player in {player1, player2}:
        if player not in defeat_mapping:
            raise ValueError("Invalid player")

    if player2 in defeat_mapping.get(player1, set()):
        return player1
    else:
        return player2

