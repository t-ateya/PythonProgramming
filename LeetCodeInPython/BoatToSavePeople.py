"""
    Given an people array and an integer limit.
    People array is an array of people's weights, i-th person has a weight people[i] and each boat can carry at most limit. Each 
    boat can carry at most 2 people at the same the same time, given that their weight sum is at most limit.
    Return the minimum number of boats require to carry every person.
"""
#My Solution
from typing import List

class Boat:
    def __init__(self, people, boat_capacity, weight_limit):
        self.people = people
        self.boat_capacity = boat_capacity
        self.weight_limit = weight_limit


    def min_num_of_boats(self):
        """Returns the max number of boats to carry people"""

#Tutor's solution
class Solution:
    def numRescueBoats(self, people: list[int], weight_limit: int) -> int:
        people.sort()
        left_pointer = 0
        right_pointer = len(people)-1
        boats_number = 0 

        while (left_pointer <= right_pointer):
            if (left_pointer == right_pointer):
                boats_number += 1
                break
            
            if (people[left_pointer] + people[right_pointer]) <= weight_limit:
                left_pointer +=1 
            
            right_pointer -= 1
            boats_number +=1

        return boats_number

people = [3, 2, 1, 3]
peo = [1,2,3,4]
sol = Solution()
print(sol.numRescueBoats(people, 3))
print(sol.numRescueBoats(peo, 4))

