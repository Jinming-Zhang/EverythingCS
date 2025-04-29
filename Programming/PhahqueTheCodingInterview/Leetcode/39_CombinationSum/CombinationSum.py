from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rawRes = self.combinationSumHelper(candidates, target)
        res = []
        for r in rawRes:
            self.addUnique(res, r)
        return res

    def combinationSumHelper(self, candidates: List[int], target: int) -> List[List[int]]:
        if (len(candidates) == 0):
            return []
        if min(candidates) > target:
            return []

        if target in candidates:
            newCandidates = candidates.copy()
            newCandidates.remove(target)

            restRes = self.combinationSumHelper(
                newCandidates, target)
            restRes.append([target])

            return restRes

        allCombos = []
        for num in candidates:
            pendingRes = self.combinationSumHelper(
                candidates, target-num)
            if len(pendingRes) > 0:
                for pending in pendingRes:
                    pending.append(num)
                    allCombos.append(pending)
        return allCombos

    def addUnique(self, lst, elmt):
        if (len(lst) == 0):
            lst.append(elmt)
            return
        elmtDict = {}
        for num in elmt:
            if num in elmtDict:
                elmtDict[num] += 1
            else:
                elmtDict[num] = 1

        contains = False
        for sol in lst:
            solDict = {}
            for num in sol:
                if num in solDict:
                    solDict[num] += 1
                else:
                    solDict[num] = 1
            if self.isSameDict(elmtDict, solDict):
                contains = True
                break
        if not contains:
            lst.append(elmt)

    def isSameDict(self, dic1, dic2):
        for k1 in dic1:
            if k1 not in dic2 or dic1[k1] != dic2[k1]:
                return False
        return True


inputs = []
inp = [[2, 3, 5], 8]
inputs.append(inp)
# inp = [[2, 3, 6, 7], 7]
# inputs.append(inp)

[print(Solution().combinationSum(r[0], r[1])) for r in inputs]
'''
Brute force:
  - Pay attention on correctly identify what the return value represent for the recursive function
'''
