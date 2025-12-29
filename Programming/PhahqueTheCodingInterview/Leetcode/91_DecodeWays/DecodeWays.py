class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        if len(s) == 2:
            if s[0] == '1':
                if s[1] == '0':
                    return 1
                else:
                    return 2
            elif s[0] == '2':
                if s[1] == '0':
                    return 1
                elif s[1] <= '6':
                    return 2
                else:
                    return 1
            else:
                if s[1] == '0':
                    return 0
                else:
                    return 1
        memo = []
        memo.append(self.numDecodings(s[0]))
        memo.append(self.numDecodings(s[:2]))
        for i in range(2, len(s)):
            res = 0
            c = s[i]
            if c >= '1' and c <= '9':
                res += memo[i-1]
            subs = s[i-1:i+1]
            if subs >= "10" and subs <= "26":
                res += memo[i-2]
            memo.append(res)
        return memo[-1]


inputs = []
s = "1201234"
inputs.append(s)
s = "12"
inputs.append(s)
s = "226"
inputs.append(s)
s = "06"
inputs.append(s)
print([Solution().numDecodings(inp)for inp in inputs])
