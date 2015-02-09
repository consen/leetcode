"""
class Solution:     # Memory Limit Exceeded
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        for i in range(0, len(s)):
            if s[i] in char_index:
                return max(i, self.lengthOfLongestSubstring(s[char_index[s[i]]+1:]))
            else:
                char_index[s[i]] = i
        return len(s)
"""

"""
class Solution:     # Runtime: 110ms
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ans = 0
        char_index = {}
        start = 0
        for i in range(0, len(s)):
            if s[i] in char_index:
                if ans < i - start:
                    ans = i - start
                end = char_index[s[i]] + 1
                for j in range(start, end):
                    del char_index[s[j]]
                start = end
            char_index[s[i]] = i
        if len(s) - start > ans:
            ans = len(s) - start 
        return ans
"""

class Solution:     # Runtime: 74ms
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ans = 0
        char_index = {}
        start = 0
        for i in range(0, len(s)):
            if s[i] in char_index and char_index[s[i]] >= start:
                if ans < i - start:
                    ans = i - start
                start = char_index[s[i]] + 1
            char_index[s[i]] = i
        if len(s) - start > ans:
            ans = len(s) - start 
        return ans

def main():
    s = Solution()
    print s.lengthOfLongestSubstring('abcabcabb')
    print s.lengthOfLongestSubstring('bbbb')
    print s.lengthOfLongestSubstring('abbc')
    print s.lengthOfLongestSubstring('aaxyzcc')
    print s.lengthOfLongestSubstring('aab')

if __name__ == '__main__':
    main()
