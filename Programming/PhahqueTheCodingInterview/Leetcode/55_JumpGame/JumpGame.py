from typing import List

'''
identify how to solve big problem with small problem
identify how to skip checks and simplify the computation
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


inputs = []
nums = [2, 3, 1, 1, 4]
inputs.append(nums)
nums = [3, 2, 1, 0, 4]
inputs.append(nums)

print([Solution().canJump(inp) for inp in inputs])

'''
update the goal from the end of the list (last index)
- if we can reach the goal at current index, then set the goal to current index
- in the next iteration, we only need to check if we can reach the goal from current index
  - if we can not, keep the goal, and there is no point to get to this index
  - if we can, set the goal to current, since we are checking backwards, there will be no situations that we can reach i+1 but not i.
'''
