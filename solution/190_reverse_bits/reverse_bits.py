class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(0, 32):
            if n & (1 << (31 - i)):
                ans += 1 << i
        return ans


def main():
    s = Solution()
    print s.reverseBits(43261596)
    print s.reverseBits(1)

if __name__ == '__main__':
    main()

