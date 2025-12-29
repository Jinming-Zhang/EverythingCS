from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        [s.add(n) for n in nums]
        if len(s) == 0:
            return 0
        length = 0
        while len(s) > 0:
            for n in s:
                if n-1 not in s:
                    segLen = 1
                    s.remove(n)
                    count = n+1
                    while (count in s):
                        s.remove(count)
                        count += 1
                        segLen += 1
                    length = max(length, segLen)
                    break
        return length


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
