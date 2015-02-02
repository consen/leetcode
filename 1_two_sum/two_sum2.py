class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hash_index = {}
        for i in range(0, len(num)):
            if num[i] in hash_index:
                return (hash_index[num[i]] + 1, i + 1)
            else:
                hash_index[target - num[i]] = i

def main():
    s = Solution()
    print s.twoSum([1, 1], 2)


if __name__ == '__main__':
    main()
