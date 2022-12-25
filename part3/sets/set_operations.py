"""
    Intersections
    {1, 2, 3} & {2, 4} -> {2}
    {1, 2, 3}.intersection({2, 4}) -> {2}
    {1, 2, 3}.intersection([2, 4])  -> {2}

    s1 & s2 & s3 & s4
    s1.intersection(s2, s3, s4)
        -> returns a new set


    Union
    {1, 2, 3} | {2, 4} -> {1, 2, 3, 4}
    {1, 2, 3}.union({2, 4}) -> {1, 2, 3, 4}
    s1 | s2 | s3 | s4
    s1.union(s2, s3, s4)
        -> returns a new set


    Disjointness
    two sets are disjoint if their intersection is empty
    len(s1 & s2)->0
      -> empty sets are falsy

    s1.isdisjoint(s2)
      ->returns a new set

    
    Differences
    {1, 2, 3, 4} - {2, 3} -> {1, 4}
    {1, 2, 3, 4}.difference({2, 3}) -> {1, 4}
    {1, 2, 3, 4}.difference([2, 3]) -> {1, 4}

    Symmetric Difference

    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}

    s1 ^ s2  -> union-intersection == (s1|s2)  - (s1 & s2) 
    s1.symmetric_difference(s2)

    s1.symmetric_difference([3, 4, 5, 6])

    s1 <= s2  -> s1.issubset(s2)
"""

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

diff = s1 ^ s2  
print(diff)