from typing import List


class Solution:
    def maxAreaSlow(self, height: List[int]) -> int:
        count = len(height)
        if count == 0 or count == 1:
            return 0
        maxArea = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j-i)*min(height[i], height[j])
                maxArea = max(maxArea, area)
        return maxArea

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area = (right - left)*min(height[left], height[right])
        while left < right:
            hl = height[left]
            hr = height[right]
            if (hl < hr):
                left += 1
            else:
                right -= 1
            area = max(area, (right - left)*min(height[left], height[right]))

        return area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))
