class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        char_word_map = {}
        word_char_map = {}
        words = str.split()
        if len(pattern) != len(words):
        	return False
        for i in range(len(pattern)):
        	if char_word_map.get(pattern[i]) == None and word_char_map.get(words[i]) == None:
        		char_word_map[pattern[i]] = words[i]
        		word_char_map[words[i]] = pattern[i]
        	elif char_word_map.get(pattern[i]) != words[i] or word_char_map.get(words[i]) != pattern[i]:
        		return False

        return True

def main():
	s = Solution()
	print(s.wordPattern("abba", "dog cat cat dog"))
	print(s.wordPattern("abba", "dog cat cat fish"))
	print(s.wordPattern("aaaa", "dog cat cat dog"))
	print(s.wordPattern("abba", "dog dog dog dog"))

if __name__ == '__main__':
	main()