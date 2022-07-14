"""
    Given an array of two integers and a target value, return the idices of 2 numbers that add up to the input target value

"""
#My Solution
class MySolution():
    def twoSum(self, arr:list[int], target:int)->list[int,int]:
        """Returns the indices of two numbers that add up to a given target"""
        temp = {}
        for index in range(0,len(arr)):
            value_to_find = target - arr[index]
            if value_to_find in temp:
                return [temp[value_to_find], index]
            temp[arr[index]] = index

sol = MySolution()
arr = [3,5,7,9,10]
print(sol.twoSum(arr, 8))