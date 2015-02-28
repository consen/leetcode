class Solution:
    # @return an integer
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        ans = 0 
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans

def main():
    s = Solution()
    print s.maxArea([1, 2, 3])
    print s.maxArea([3, 2, 1])
    print s.maxArea([10, 5, 1, 5, 1, 1])


if __name__ == '__main__':
    main()
