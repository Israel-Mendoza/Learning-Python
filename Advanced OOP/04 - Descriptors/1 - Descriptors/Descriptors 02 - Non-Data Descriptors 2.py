from __future__ import annotations
from typing import Any
from random import choice


"""Using a non-data descriptor as a random choice picker"""


class RandomItemGetter:

    def __init__(self, *args: str) -> None:
        """
        Storing the sequence from which the __get__ method will randomly return an item
        """
        print(f"Creating a Choice non-data descriptor with the following sequence: \n\t{args}")
        self.sequence: tuple[[str], ...] = args

    def __get__(self, instance: Any, owner: type) -> any:
        """Returning a random item from the self.sequence"""
        return choice(self.sequence)


class Deck:

    """A class to represent a simple card deck"""

    # Non-Data Descriptor instances:
    suits: RandomItemGetter = RandomItemGetter("Spades", "Hearts", "Diamonds", "Clubs")
    card: RandomItemGetter = RandomItemGetter(*tuple("23456789AKJQ"), "10")

    def __init__(self, deck_name: str) -> None:
        """Initialized the deck with a name"""
        self.deck_name: str = deck_name

    def get_card(self) -> str:
        """Returns a string representing a random card"""
        # Notice how this method is accessing both 
        # Non-Data descriptors in the class. The __get__ method
        # returns a random item contained in their self.sequence attribute
        return f"{self.card:2} of {self.suits}"


# Creating a Choice non-data descriptor with the following sequence:
# 	('Spades', 'Hearts', 'Diamonds', 'Clubs')
# Creating a Choice non-data descriptor with the following sequence:
# 	('2', '3', '4', '5', '6', '7', '8', '9', 'A', 'K', 'J', 'Q', '10')


# Instantiating a Deck
my_deck: Deck = Deck("My English Deck")

# Calling the get_card() method, which accesses both 
# descriptor instances, "suite" and "card" via the Deck instance
for _ in range(10):
    print(my_deck.get_card())
# K  of Diamonds
# 4  of Diamonds
# 10 of Hearts
# A  of Diamonds
# Q  of Spades
# 10 of Hearts
# 7  of Clubs
# Q  of Hearts
# J  of Clubs
# 8  of Hearts
