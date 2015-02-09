class Solution:
    def largestNumber(self, num):
        ans = ''
        count = len(num)
        for i in range(0, count):
            first_num = self.getFirstNumber(num)
            ans += str(first_num)
            num.remove(first_num)
        return str(int(ans))        # str(int()) for [0, 0]

    def getFirstNumber(self, num):
        first_num = num[0]
        for i in num:
            first_num = first_num if str(first_num) + str(i) > str(i) + str(first_num) else i
        return first_num


def main():
    s = Solution()
    print s.largestNumber([3, 30, 34, 5, 9])
    print s.largestNumber([0, 0])
    print s.largestNumber([1, 0, 0])
    print s.largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247])


if __name__ == '__main__':
    main()
