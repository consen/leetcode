class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num.sort()
        return num[len(num) / 2]


def main():
    s = Solution()
    print s.majorityElement([1, 2, 1, 1])

if __name__ == '__main__':
    main()
