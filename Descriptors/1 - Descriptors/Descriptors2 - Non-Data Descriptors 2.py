"""Using a non-data descriptor as a random choice picker"""


from random import choice
from typing import Any, Sequence


class Choice:

    def __init__(self, *args: Sequence[Any]) -> None:
        """
        Storing the sequence from which the __get__
        method will randomly return an item
        """
        print(f"Creating a Choice non-data descriptor with the following sequence: {args}")
        self.sequence = args

    def __get__(self, instance, owner) -> Any:
        """Returning a random item from the self.sequence"""
        return choice(self.sequence)


class Deck:

    """A class to represent a simple card deck"""

    # Non-Data Descriptor instances:
    suits = Choice("Spades", "Hearts", "Diamonds", "Clubs")
    card = Choice(*tuple("23456789AKJQ"), "10")

    def __init__(self, deck_name: str) -> None:
        """Initialized the deck with a name"""
        self.deck_name = deck_name

    def get_card(self) -> str:
        """Returns a string representing a random card"""
        # Notice how this method is accessing both 
        # Non-Data Descriptors in the class, which __get__
        # method returns a random item in their self.sequence attribute
        return f"{self.card:2} of {self.suits}"


# Creating a Choice non-data descriptor with the following sequence: ('Spades', 'Hearts', 'Diamonds', 'Clubs')
# Creating a Choice non-data descriptor with the following sequence: ('2', '3', '4', '5', '6', '7', '8', '9', 'A', 'K', 'J', 'Q', '10')


# Instanciating a Deck
my_deck = Deck("My English Deck")

# Calling the get_card() method, which accesses both 
# descriptor instances, "suite" and "card" via the Deck instance
for _ in range(10):
    print(my_deck.get_card())
# 4  of Diamonds
# 4  of Hearts
# 4  of Diamonds
# 6  of Spades
# 9  of Clubs
# 2  of Clubs
# 10 of Diamonds
# 2  of Hearts
# 6  of Clubs
# 7  of Diamonds
