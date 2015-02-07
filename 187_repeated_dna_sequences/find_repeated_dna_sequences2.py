class Solution:
    def findRepeatedDnaSequences(self, s):
        """
            repeated DNA can be overlaped.
            'AAAAAAAAAAA'  ('A'*11)
            return ['AAAAAAAAAA'] ('A'*10)
        """
        dna_count = dict()
        for i in [s[x:x+10] for x in range(0, len(s)-9)]:
            dna_count[i] = dna_count.get(i, 0) + 1
        return [k for k, v in dna_count.iteritems() if v > 1]

def main():
    s = Solution()
    print s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    print s.findRepeatedDnaSequences('AAAAAAAAAAAAAAA')

if __name__ == '__main__':
    main()
