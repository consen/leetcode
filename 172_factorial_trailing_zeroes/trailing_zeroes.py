"""
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        count_2 = 0
        count_5 = 0
        for i in range(1, n + 1):
            while i % 5 == 0:
                count_5 += 1
                i /= 5
            while i % 2 == 0:       # Time Limit Exceeded
                count_2 += 1
                i /= 2
        return min(count_2, count_5)
"""

"""
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        count_5 = 0
        for i in range(1, n + 1):   # MemoryError
            while i % 5 == 0:
                count_5 += 1
                i /= 5
        return count_5
"""

"""
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        count_5 = 0
        i = 1
        while i < n + 1:            # Time Limit Exceeded
            j = i
            while j % 5 == 0:
                count_5 += 1
                j /= 5
            i += 1
        return count_5
"""

class Solution:
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        return n / 5 + self.trailingZeroes(n / 5)

def main():
    s = Solution()
    print s.trailingZeroes(1)
    print s.trailingZeroes(5)
    print s.trailingZeroes(100)
    print s.trailingZeroes(1808548329)

if __name__ == '__main__':
    main()
