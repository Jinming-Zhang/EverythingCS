from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)

        return res

    def maxSubArraySlow(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = nums[0]
        for i in range(0, len(nums)):
            sum = nums[i]
            res = max(res, sum)
            for j in range(i+1, len(nums)):
                sum += nums[j]
                res = max(res, sum)
        return res


inputs = []
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
inputs.append(nums)
nums = [1]
inputs.append(nums)
nums = [5, 4, -1, 7, 8]
inputs.append(nums)
nums = [-2, -1]
inputs.append(nums)

print([Solution().maxSubArray(inp) for inp in inputs])
