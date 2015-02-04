class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num_count = {}
        for i in num:
            if i in num_count:
                num_count[i] += 1
            else:
                num_count[i] = 1
            if num_count[i] > (len(num) / 2):
                return i                


def main():
    s = Solution()
    print s.majorityElement([1, 2, 1, 1])

if __name__ == '__main__':
    main()
