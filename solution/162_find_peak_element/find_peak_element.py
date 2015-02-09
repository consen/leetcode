class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 1:
            return 0
        if num[0] > num[1]:
            return 0
        if num[-1] > num[-2]:
            return len(num) - 1 
        
        """ not Time Limit Exceeded
        for i in range(0, len(num) - 1):
            if num[i] > num[i + 1]:
                return i
        """
        
        left = 0
        right = len(num) - 1
        while left < right:
            mid = (left + right) / 2
            if num[mid] < num[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return right

def main():
    s = Solution()
    print s.findPeakElement([0])
    print s.findPeakElement([1, 0])
    print s.findPeakElement([0, 1])
    print s.findPeakElement([1, 2, 3, 2])
    print s.findPeakElement([1, 6, 5, 4, 3, 2, 1])
    print s.findPeakElement([1, 2, 1])

if __name__ == '__main__':
    main()
