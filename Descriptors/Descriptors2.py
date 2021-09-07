"""Using a non-data descriptor as a random choice picker"""


from random import choice
from typing import Any, Sequence


class Choice:

    def __init__(self, *args: Sequence[Any]) -> None:
        """
        Storing the sequence from which the __get__
        method will randomly return an item
        """
        self.sequence = args

    def __get__(self, instance, owner) -> Any:
        """Returning a random item from the self.sequence"""
        return choice(self.sequence)


class Deck:

    """A class to represent a simple card deck"""

    suits = Choice("Spades", "Hearts", "Diamonds", "Clubs")
    card = Choice(*tuple("23456789AKJQ"), "10")

    def __init__(self, deck_name: str) -> None:
        """Initialized the deck with a name"""
        self.deck_name = deck_name

    def get_card(self) -> str:
        """Returns a string representing a random card"""
        return f"{self.card:2} of {self.suits}"


# Instanciating a Deck
my_deck = Deck("My English Deck")

# Calling the get_card() method, which accesses
# both descriptor instances, "suite" and "card"
# via the Deck instance
for _ in range(10):
    print(my_deck.get_card())
# Q  of Hearts
# A  of Spades
# J  of Spades
# J  of Clubs
# 10 of Clubs
# 6  of Diamonds
# 5  of Hearts
# K  of Hearts
# 5  of Diamonds
# 6  of Diamonds
