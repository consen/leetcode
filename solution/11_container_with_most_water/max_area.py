"""
class Solution:     # Time Limit Exceeded
    # @return an integer
    def maxArea(self, height):
        ans = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                tmp = (j-i) * min(height[i], height[j])
                if ans < tmp:
                    ans = tmp
        return ans
"""

"""
class Solution:     # Time Limit Exceeded
    # @return an integer
    def maxArea(self, height):
        ans = 0
        left = 0
        for i in range(0, len(height)):
            if height[i] <= left:
                continue
            else:
                left = height[i]
            for j in range(i+1, len(height)):
                tmp = (j-i) * min(height[i], height[j])
                if ans < tmp:
                    ans = tmp
        return ans
"""


class Solution:     # Time Limit Exceeded
    # @return an integer
    def maxArea(self, height):
        if len(height) == 1:
            return 0
        if len(height) == 2:
            return min(height[0], height[1]) * (1 - 0)
        ans = min(height[0], height[1]) * (1 - 0)
        for i in range(2, len(height)):
            for j in range(0, i):
                ans = max(ans, min(height[i], height[j]) * (i - j))
                if height[j] >= height[i]:
                    break
        return ans

def main():
    s = Solution()
    print s.maxArea([1, 2, 3])
    print s.maxArea([3, 2, 1])


if __name__ == '__main__':
    main()
