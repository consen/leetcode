class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        self.num = [0, 0] + num
        self.total = [None] * (len(self.num) + 3)
        return self.dfs(0)

    def dfs(self, index):
        if self.total[index] != None:
            return self.total[index]
        if index >= len(self.num):
            return 0
        left = self.dfs(index+2)
        right = self.dfs(index+3)
        self.total[index] = self.num[index]
        self.total[index] += left if left >= right else right
        return self.total[index]


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
