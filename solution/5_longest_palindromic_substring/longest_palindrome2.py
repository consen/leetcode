class Solution:
    # @return a string
    def longestPalindrome(self, s):
        start = 0
        length = 0
        for i in range(0, len(s)):
            if self.isPalindrome(s[i-length:i+1]):
                start = i-length
                length += 1
            if i-length-1 >= 0 and self.isPalindrome(s[i-length-1:i+1]):
                start = i-length-1
                length += 2
        return s[start:start+length]

    def isPalindrome(self, s):
        return s == s[::-1]

def main():
    s = Solution()
    print s.longestPalindrome('a')
    print s.longestPalindrome('aa')
    print s.longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaa')
    print s.longestPalindrome('xabccbay')
    print s.longestPalindrome('xabcbay')

if __name__ == '__main__':
    main()
