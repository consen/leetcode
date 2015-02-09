class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s

        ans = [''] * nRows
        index = 0
        step = 1
        for i in range(0, len(s)):
            ans[index] += s[i]
            if index == nRows - 1:
                step = -1
            elif index == 0:
                step = 1
            index += step

        return ''.join(ans)