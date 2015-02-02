class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        count = len(num)
        for i in range(0, count):
            for j in range(i + 1, count):
                if (num[i] + num[j] == target):
                    return (i+1, j+1)

def main():
    s = Solution()
    print s.twoSum([1, 1], 2)


if __name__ == '__main__':
    main()
