import collections
import random

# Declaring a Card
Card = collections.namedtuple("Card", ["rank", "suit"])


class Deck:

    ranks: list[str] = [str(number) for number in range(2, 11)] + list("JQKA")
    suits: list[str] = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards: list[Card] = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self) -> int:  # __len__ and __getitem__ make the deck iterable
        return len(self._cards)

    def __getitem__(self, item: int | slice) -> Card:  # __len__ and __getitem__ make the deck iterable
        return self._cards[item]


def card_value(card: Card) -> int:
    """Returns an int containing the absolute value of the passed card"""
    suit_values: dict[str, int] = {"spades": 3, "hearts": 2, "diamonds": 2, "clubs": 1}
    rank_value: int = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# A random card:
print(f"A random card: {random.choice(Deck())}")
# A random card: Card(rank='J', suit='diamonds')

sorted_cards: list[Card] = sorted(Deck(), key=card_value)

for card in sorted_cards:
    print(card)
# Card(rank='2', suit='clubs')
# Card(rank='2', suit='diamonds')
# Card(rank='2', suit='hearts')
# Card(rank='2', suit='spades')
# Card(rank='3', suit='clubs')
# Card(rank='3', suit='diamonds')
# . . .
# Card(rank='A', suit='diamonds')
# Card(rank='A', suit='hearts')
# Card(rank='A', suit='spades')
