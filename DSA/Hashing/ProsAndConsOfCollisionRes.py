"""
    1. Direct Chaining
            Pros
        - Hash table never gets full
            Cons
        - Huge Linked List causes performance leaks (Time complexity for search operation becomes O(n))
    2. Open Addressing
        - Easy Implementation
        - When Hash Table is Full, creation of new Hash Table affects performance(Time complexity for search operation becomes O(N))

        When to use each technique:
            If the input size is known, we always use "Open Addressing"
            If we perform deletion operation frequently, we use "Direct Chaining"
"""