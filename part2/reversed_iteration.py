"""
    Iterating a sequence in reverse order
     If we have a sequence type, then iterating over the sequence in reverse order is quite simple:
        for item in seq[::-1]:
            print(item)              ->Works but wasteful because it makes a copy of the sequence

    for item in seq[::-1]:
        print(item)

    for i in range(len(seq)):
        print(seq[len(seq) -i -1])

    for i in range(len(seq)-1, -1, -1):
        print(seq[i])                       more efficient but syntan messy

    Using python built-in
    for item in reversed(seq):
        print(item)


    We can override how reversed works by implementing the __reversed__ special method

    Iterating an iterable in reverse
        Unfortunately, reversed() will not work with custom iterables without a lit bit of extra work

    When we call reversed() on a custom iterable, Python will look for and call the __reversed__ function. 
    That function should return an iterator that will be used to perform the reverse iteration.

    Just like the iter() method, when we call reversed() on an object:
        python looks for and calls __reversed__ method
        if it's not there, it uses __getitem__ and __len__ to create an iterator for us

seq = [1,2,3,4]
for item in reversed(seq):
    print(item)


Card Deck Example

    In the code exercises, we will build an iterable containing a deck of 52 sorted cards.
    2Spades...Ace Spades, 2 Hearts...Ace Hearts, 2 Diamonds...Ace Diamonds, 2Clubs...Ace Clubs
    but we don't want to create a list containing all the pre-created cards ->Lazy evaluation

    SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    RANKS = [2, 3, ..., 10, 'J', 'Q', 'K', 'A']
    2S...AS 2H...AH 2D...AD 2C...AC

    We assume the deck is sorted as follows:
        iterate over SUITS
            for each suit, iterate over RANKS
                card = combination of suit and rank

    There are len(SUITS) suits ==4 and there're len(RANKS) ranks == 13
    The deck has a length of: len(SUITS)*len(RANKS) == 52
    Each card in this deck has a positional index: a number from 0 to len(deck)-1

    To find the suit index of a card at index i:
    i//len(RANKS)
        Examples
    5th card (6S)->index 4
    ->4 // 13 ->0
    16th card (4H)->index 15
        -> 15//13 ->1

    To find the rank index of a card at index i:
        i % len(RANKS)
        Examples
        5th card(6S)->index 4
            -> 4 % 13 ->4
        16th card (4H) ->index 15
            -> 15 % 13 ->2

    (JKQA)-> Jack, Queen, King, Ace


    Note:
        Python reversed() method can automatically reverse a sequence type and not a general iterable. 
        But the sequence type must have the __len__() implemented.
        You must override the reversed() or re-define reverse in the __next__ method method in your iterable in order for python to recognize
         See the examples of Squares and CardDeck below
"""


#global variable
_SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
_RANKS = tuple(range(2,11)) + tuple("JQKA")

from collections import namedtuple
Card = namedtuple('Card', 'rank suit')

class CardDeck:
    """Iterable"""
    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.CardDeckIterator(self.length)

    def __reversed__(self):
        return self.CardDeckIterator(self.length, reverse = True)

    class CardDeckIterator:
        #Lazy Evaluation since we didn't pre-create the deck
        def __init__(self, length, reverse = False):
            self.legth = length
            self.index = 0
            self.reverse = reverse

        def __iter__(self):
            return self 

        def __next__(self):
            if self.index >= self.legth:
                raise StopIteration
            else:
                if self.reverse:
                    i = self.legth - 1 - self.index
                else:
                    i = self.index
                suit = _SUITS[i // len(_RANKS)]
                rank = _RANKS[i % len(_RANKS)]
                self.index += 1
                return Card(rank, suit)
            


deck = CardDeck()

"""
for card in deck:
    print(card)
"""

deck = list(CardDeck())
#print(deck)
#print(deck[:-8:-1])

reversed_deck = reversed(CardDeck())

for c in reversed_deck:
    print(c)



#reverse in sequences
class Squares:
    """Implementing sequence reverse without overriding the __reverse__ method. Python automatically uses __len__() to reverse the sequence"""
    def __init__(self, length):
        self.squares = [x**2 for x in range(length)]

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, s):
        return self.squares[s]  #Delegation

"""
for num in Squares(5):
    print(num)

for num in reversed(Squares(5)):
    print(num)
"""


#Overriding reverse method

class Squares:
    """Implementing sequence reverse by overriding the __reversed__ method"""
    def __init__(self, length):
        self.squares = [x**2 for x in range(length)]

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, s):
        return self.squares[s]  #Delegation

    def __reversed__(self):
        print("__reversed__ called")
        return 'Hello Python'

for num in reversed(Squares(5)):
    print(num)