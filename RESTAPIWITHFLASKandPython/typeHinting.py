from typing import List

def list_avg(sequence:list)->float:
    return sum(sequence)/ len(sequence)


seq = [1, 2, 3, 4,]
print(list_avg(seq))



class Book:
    pass 

class BookShelf:
    def __init__(self, books: List[Book]):
        pass

