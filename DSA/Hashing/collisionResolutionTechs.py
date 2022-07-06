
"""
    Collision can be resolved by using 2 techniques:
    1. Direct Chaining
         - Implements the bucket as linked list. Colliding elements are stored in this list
    2. Open Addressing
            Colliding elements are stored in other vacant buckets. During storage and lookup, these are found through so called probing
        - Linear Probing
            * It places new key into closest following cell(closest next cell)
        - Quadractic Probing
            *Adding arbitrary quadratic polynomial to the index until an empty cell is found
        - Double Hashings
            * Interval between probes is computed by another hash function
"""