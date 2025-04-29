from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 10:
            if target in nums:
                return nums.index(target)
            else:
                return -1

        pivot = self.findPivotInd(nums, 0, len(nums)-1)
        left = pivot+1
        right = pivot + len(nums)
        while (left <= right):
            middle = int((right+left)/2)
            middleConverted = middle % len(nums)
            middleNum = nums[middleConverted]
            if (middleNum == target):
                return middleConverted
            else:
                if target > middleNum:
                    left = middle + 1
                else:
                    right = middle-1
        return -1

    def findPivotInd(self, nums: List[int], left: int, right: int) -> int:
        if left > right:
            return -1
        middleInd = int((right+left)/2)
        prev = middleInd - 1
        if prev < 0:
            prev = len(nums)-1
        next = middleInd+1
        if next >= len(nums):
            next = 0
        prev = nums[prev]
        next = nums[next]
        middle = nums[middleInd]
        if prev > middle or middle > next:
            return middleInd
        res = self.findPivotInd(nums, left, middleInd-1)
        if res != -1:
            return res
        res = self.findPivotInd(nums, middleInd+1, right)
        return res


inputs = []
inputs.append([[266, 267, 268, 269, 271, 278, 282, 292, 293, 298, 6, 9, 15, 19, 21, 26, 33, 35, 37, 38, 39, 46, 49, 54, 65, 71, 74, 77, 79, 82, 83, 88, 92, 93, 94, 97, 104, 108, 114, 115, 117, 122, 123, 127,
              128, 129, 134, 137, 141, 142, 144, 147, 150, 154, 160, 163, 166, 169, 172, 173, 177, 180, 183, 184, 188, 198, 203, 208, 210, 214, 218, 220, 223, 224, 233, 236, 241, 243, 253, 256, 257, 262, 263], 208])
inputs.append([[1], 0])
print([Solution().search(inp[0], inp[1]) for inp in inputs])
