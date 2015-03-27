class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        weight = 0
        while n:
            weight += 1
            n &= n - 1
        return weight

def main():
    s = Solution()
    print s.hammingWeight(11)

if __name__ == '__main__':
    main()
