"""
    A binary heap is a binary tree with the following properties:

    -A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be min among all keys present in Binary Heap
       The same property must be recursively true for all nodes in Binary Tree.
    -It's a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This
    property of Binary Heap makes them suitable to be stored in an array


    ########## Why Binary Heap?  ############
    Find the minimum or maximum number among a set of numbers in logN time. And also we want to make sure that inserting additional numbers does not take 
    more than O(logN) time complexity
      Possible Solutions:
        1. Store the numbes in sorted Array
            Find minimum: O(1)
            Insertion: O(n)
        2. Store the numbers in linkedList in sorted manner
              Insertion: O(n)


        Practical Use of Binary Heap:
            -Prim's Algorithm
            - Heap Sort
            - Priority Queue


    Types of Binary Heap:
        Min Heap - The value of each node is less than or equal to the value of both its children (parentNode <= childNode)
        Max Heap - It's exactly the opposite of min heap. I.e the value of each node is greater than or equal to the value of both its children (parentNode > ChildNode)
"""