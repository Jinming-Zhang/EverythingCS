from typing import List


class Solution:
    def sameTriplet(self, t1, t2):
        t1dic = {}
        for i in t1:
            if i in t1dic:
                t1dic[i] = t1dic[i] + 1
            else:
                t1dic[i] = 1
        t2dic = {}
        for i in t2:
            if i in t2dic:
                t2dic[i] = t2dic[i] + 1
            else:
                t2dic[i] = 1

        for i in t2:
            if i not in t1dic:
                return False
            elif t1dic[i] != t2dic[i]:
                return False
        return True

    def tryAppend(self, list, t):
        for e in list:
            if self.sameTriplet(e, t):
                return
        list.append(t)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        if len(nums) < 3:
            return
        prevn = nums[0]
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == prevn:
                continue
            prevn = nums[i]
            n = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                jn = nums[j]
                kn = nums[k]
                sum = n + nums[j] + nums[k]
                if sum > 0:
                    while k > 0 and nums[k] == kn:
                        k -= 1
                elif sum < 0:
                    while j < len(nums) and nums[j] == jn:
                        j += 1
                else:
                    res = [n, jn, kn]
                    sol.append(res)
                    while j < len(nums) and nums[j] == jn:
                        j += 1
                    while k > 0 and nums[k] == kn:
                        k -= 1
        return sol

    def threeSumSlow(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return 0
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):

                        self.tryAppend(res, ([nums[i], nums[j], nums[k]]))
        return res


inputs = []
nums = [-1, 0, 1, 2, -1, -4]
inputs.append(nums)

print([Solution().threeSum(inp) for inp in inputs])
