from typing import *
from Utils import FuncTimeEval


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = 0
        for i in range(0, len(s)):
            substr = s[i:]
            m = max(m, self.longestValidParenthesesStart(substr))
        return m

    def longestValidParenthesesStart(self, s: str, cached={}) -> int:
        if len(s) <= 1:
            return 0
        if s[0] == ')':
            return self.longestValidParenthesesStart(s[1:])

        leftCount = 1
        rightCount = 0
        result = 0
        if s in cached:
            return cached[s]

        for j in range(1, len(s)):
            c = s[j]
            if c == '(':
                leftCount += 1
            if c == ')':
                rightCount += 1

            if leftCount == rightCount:
                if j == len(s) - 1:
                    cached[s] = len(s)
                    return len(s)
                substr = s[j+1:]
                if (len(substr) == 0):
                    cached[s] = len(s)
                    return len(s)

                if substr[0] == ')':
                    cached[s] = j+1
                    return j+1
                else:
                    result = j+1 + \
                        self.longestValidParenthesesStart(substr, cached)
                    cached[s] = result
                    return result
        cached[s] = result
        return result


if (__name__ == "__main__"):
    # print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses(")()())()()("))
