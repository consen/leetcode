class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        reverse = 0
        n = abs(x)
        while n:
            reverse = reverse * 10 + n % 10
            n /= 10
        return reverse == x