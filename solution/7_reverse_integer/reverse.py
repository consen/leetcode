class Solution:
    # @return an integer
    def reverse(self, x):
        flag = True if x < 0 else False
        ans = 0
        x = abs(x)
        while x:
        	ans = ans * 10 + x % 10
        	x /= 10
        ans = -ans if flag else ans
        if ans > 2147483647 or ans < -2147483648:
        	ans = 0
        return ans
