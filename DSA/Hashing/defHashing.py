"""
        Outline
    1.Hash Functions
    2. Collision Resolution Techniques
    3. Hash Tables
    4. Practical use of Hashing

        Definition
    Hashing is a method of sorting and indexing data. The idea behind hashing is to allow large amounts of data to be indexex
    using keys commonly created by using formulas
        Example:
        Let's assume we the strings: "Apple", "Application" and "Appmillers" and we wanna sort them in an efficient way

        Why Hashing?
        - Used in developing an app in which the SEARCH operation is used heavily and we want our app to perform as fast as possible(
            It's time efficient in case of SEARCH OPERATION
        )



    Hashing Terminologies
    1. Hash Function(magic function)
        - It's a function that can be used to map data of arbitrary size to data of fixed size

    2. Key
        - Input data given by the user (any data provided to the magic function)

    3. Hash Value: A value that is returned by Hash Function
            - Also called hash codes, digest or simply hash
    4. Hash Table
        - A data structure which implements an associative array abstract data type, a structure that can map keys to values.

    5. Collision: Occurs when two different keys to a hash function produce same output (hash value)


    Properties of good hash Function:
      1. It distributes hash values uniformly across hash functions
      2. It has to use all input data
      3. 
"""
