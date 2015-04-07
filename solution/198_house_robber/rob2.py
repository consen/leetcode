class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        """
        dp[n] = max(dp[n-1], dp[n-2] + num[n])
        """
        if not num:
            return 0
        if len(num) == 1:
            return num[0]
        dp = [0] * len(num)
        dp[0] = num[0]
        dp[1] = max(num[0], num[1])
        for i in range(2, len(num)):
            dp[i] = max(dp[i-1], dp[i-2] + num[i])
        return dp[len(num)-1]


if __name__ == '__main__':
    s = Solution()
    print s.rob([1])
    print s.rob([1, 2])
    print s.rob([1, 2, 3])
    print s.rob([1, 5, 3])
    print s.rob([0, 0, 0, 0])
    print s.rob([4, 1, 2, 7, 5, 3, 1])
    print s.rob([1, 2, 1, 1])
    print s.rob([1, 2, 1, 2])
