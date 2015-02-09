class Solution:
    def findRepeatedDnaSequences(self, s):
        """
            repeated DNA can be overlaped.
            'AAAAAAAAAAA'  ('A'*11)
            return ['AAAAAAAAAA'] ('A'*10)
        """
        dna_count = dict()
        dna_repeated = set()
        for x in range(0, len(s) - 9):
            dna = s[x:x+10]
            if dna in dna_count:
                dna_count[dna] += 1
            else:
                dna_count[dna] = 1
            if dna_count[dna] > 1:
                dna_repeated.add(dna)
        return list(dna_repeated)


def main():
    s = Solution()
    print s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    print s.findRepeatedDnaSequences('AAAAAAAAAAAAAAA')

if __name__ == '__main__':
    main()
