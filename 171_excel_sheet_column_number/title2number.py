class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num = 0
        s = s[::-1]
        for i in range(0, len(s)):
            num += (ord(s[i]) - ord('A') + 1) * (26 ** i)
        return num

def main():
    s = Solution()
    print s.titleToNumber('A')
    print s.titleToNumber('Z')
    print s.titleToNumber('AA')
    print s.titleToNumber('AB')
    print s.titleToNumber('ZZ')

if __name__ == '__main__':
    main()

