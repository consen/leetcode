class Solution:
    # @return a string
    def convertToTile(self, num):
        ans = ''
        while num:
            num -= 1
            ans += chr(num % 26 + ord('A'))
            num = num / 26
        return ans[::-1]

def main():
    s = Solution()
    print s.convertToTile(1)
    print s.convertToTile(26)
    print s.convertToTile(27)

if __name__ == '__main__':
    main()
