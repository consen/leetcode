"""
class Solution:     # Time Limit Exceeded
    # @return a string
    def longestPalindrome(self, s):
        longest = '' 
        for i in range(1, len(s)):
            for j in range(i-1, -1, -1):
                if i+(i-j) < len(s) and s[j] == s[i+(i-j)]:
                    if len(longest) < 2 * (i-j) + 1:
                        longest = s[j:i+(i-j)+1]
                else:
                    break
            for j in range(i, -1, -1):
                if i+(i-j+1) < len(s) and s[j] == s[i+(i-j+1)]:
                    if len(longest) < 2 * (i-j+1):
                        longest = s[j:i+(i-j+1)+1]
                else:
                    break
        return longest if longest else s
"""

"""
class Solution:     # Time Limit Exceeded
    # @return a string
    def longestPalindrome(self, s):
        start, end = 0,0  
        for i in range(1, len(s)):
            for j in range(i-1, -1, -1):
                if i+(i-j) < len(s) and s[j] == s[i+(i-j)]:
                    if end-start+1 < 2 * (i-j) + 1:
                        start, end = j, i+(i-j)+1
                else:
                    break
            for j in range(i, -1, -1):
                if i+(i-j+1) < len(s) and s[j] == s[i+(i-j+1)]:
                    if end-start+1 < 2 * (i-j+1):
                        start, end = j, i+(i-j+1)+1
                else:
                    break
        return s[start:end] if end-start != 0 else s 
"""

"""
class Solution:     # Time Limit Exceeded
    # @return a string
    def longestPalindrome(self, s):
        ans = ''
        start, end = 0, 0  
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                start, end = i, j 
                while start <= end:
                    if s[start] == s[end]:
                        start += 1
                        end -=1
                    else:
                        break
                if start > end and len(ans) < j-i+1:
                    ans = s[i:j+1]
        return ans
"""

"""
class Solution:     # Time Limit Exceeded
    # @return a string
    def longestPalindrome(self, s):
        ans = ''
        start, end = 0, 0  
        for i in range(0, len(s)):
            for j in range(len(s)-1, i-1, -1):
                start, end = i, j 
                while start <= end:
                    if s[start] == s[end]:
                        start += 1
                        end -=1
                    else:
                        break
                if start > end and len(ans) < j-i+1:
                    ans = s[i:j+1]
                    break
        return ans
"""

class Solution:     # Time Limit Exceeded
    # @return a string
    def longestPalindrome(self, s):
        ans = ''
        start, end = 0, 0  
        for i in range(0, len(s)):
            if len(ans) > len(s)-i+1:
                break
            for j in range(len(s)-1, i-1, -1):
                if len(ans) > j-i+1:
                    break
                start, end = i, j 
                while start <= end:
                    if s[start] == s[end]:
                        start += 1
                        end -=1
                    else:
                        break
                if start > end and len(ans) < j-i+1:
                    ans = s[i:j+1]
                    break
        return ans

def main():
    s = Solution()
    print s.longestPalindrome('a')
    print s.longestPalindrome('aa')
    print s.longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaa')
    print s.longestPalindrome('xabccbay')
    print s.longestPalindrome('xabcbay')

if __name__ == '__main__':
    main()
