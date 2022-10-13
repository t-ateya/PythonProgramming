def square(n):
    for i in range(n):
        yield i**2


sq = square(5)
print(next(sq))
print(next(sq))
print(next(sq))

enum1 = enumerate(sq)
print(list(enum1))

#print(next(sq))
#print(next(sq))


print("================================")
for s in sq:
    print(s)


#Generator function
def square_gen(n):
    for i in range(n):
        yield i ** 2

#iterable
class Squares:
    def __init__(self, n) -> None:
        self.n = n 

    def __iter__(self):
        return Squares.square_gen(self.n)

    @staticmethod
    def square_gen(n):
        for i in range(n):
            yield i** 2


sq = Squares(5)
for num in sq:
    print(num)

print(list(sq))

#   ================================================
from collections import namedtuple
Card = namedtuple('Card', 'rank suit')

class CardDeck:
    SUITS =('Spades', 'Hearts', 'Diamonds', 'Clubs')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')

    def __iter__(self):
        return CardDeck.card_gen()

    def __reversed__(self):
        return CardDeck.reversed_card_gen()

    @staticmethod
    def card_gen():
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                yield Card(rank, suit)

    @staticmethod
    def reversed_card_gen():
        for suit in reversed(CardDeck.SUITS):
            for rank in reversed(CardDeck.RANKS):
                yield Card(rank, suit)