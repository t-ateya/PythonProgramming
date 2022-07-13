"""
#278S
    You have N versions of software, we want to find the first "bad" version of the software
    Note: If a version is bad, all versions that come after it are bad.

    Hint:
    The isBadVersion API is already defined for you.
    @param version, an integer
    @return a bool
    def isBadVersion(version)

"""

#My Solution

def isBadVersion(n:int)->bool:
        return n>=5

class MySolution:
    def isBadVersion(self, n:int)->bool:
        return n>=19
    def solution(self, arr:list[int]) ->int:
        left = 0
        right = len(arr)-1
        if (self.isBadVersion(arr[left])):
            return arr[left]

        while (left <= right):
            mid = (left + right)//2
            if (self.isBadVersion(arr[mid])):
                if not (self.isBadVersion(arr[mid -1])):
                    return arr[mid] 
                right = mid 
            else:
                left = mid 
                if left == right-1:
                    return arr[right]



#Tutor's solution
class Solution:
    def firstBadVersion(self, n):
        left = 1;
        right = n;
        while (left < right):
            mid = (right + left)//2;
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid;
        return left




sol = Solution()
#arr = [1,2,3,4,5,6,10,11,12,13,16,17,18,19]
print(sol.firstBadVersion(9))

                
            

