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
