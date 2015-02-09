class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s

        ans = [''] * nRows
        x = 0
        y = 1
        for i in range(0, len(s)):
            if (i / (nRows - 1)) % 2 == 0:  # down
                y = 1
                ans[x] += s[i]
                x += 1
            else:                           # up
                x = 0
                ans[-y] += s[i]
                y += 1
        return ''.join(ans)