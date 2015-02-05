class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.') 
        v2 = version2.split('.')
        v1 = map(int, v1)
        v2 = map(int, v2)
        if (len(v1) < len(v2)):
            v1.extend([0] * (len(v2) - len(v1)))
        else:
            v2.extend([0] * (len(v1) - len(v2)))
        
        for i in range(0, len(v1)):
            if (v1[i] == v2[i]):
                continue
            elif (v1[i] < v2[i]):
                return -1
            elif (v1[i] > v2[i]):
                return 1
            
        return 0

def main():
    s = Solution()
    print s.compareVersion('0.1', '1.1')
    print s.compareVersion('1.1', '1.2')
    print s.compareVersion('1.2', '13.37')
    print s.compareVersion('01', '1')
    print s.compareVersion('10.6.5', '10.6')

if __name__ == '__main__':
    main()

