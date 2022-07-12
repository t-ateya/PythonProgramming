"""
    Given n non-negative integers where each integer represents the height of a vertical line on a chart, Find two lines, which together with x-axis
    forms a container that holds the biggest amount of water. Return the area of that water
"""
class Solution:
    def maxArea(self, height: list[int]) ->int:
        left = 0
        right = len(height) -1
        max_area = 0

        while(left < right):
            area = min(height[left], height[right])*(right - left)
            max_area = max(max_area, area)

            if (height[left] < height[right]):
                left +=1
            else:
                right -=1
        return max_area


sol = Solution()
height = [1,8,6,2,5,7]
print(sol.maxArea(height))
