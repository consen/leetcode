class Solution:
    def largestNumber(self, num):
        num = map(str, num)
        num.sort(cmp=lambda a, b: 1 if a+b > b+a else -1 if a+b<b+a else 0,
                 reverse=True)
        return str(int(''.join(num)))

def main():
    s = Solution()
    print s.largestNumber([3, 30, 34, 5, 9])
    print s.largestNumber([0, 0])
    print s.largestNumber([1, 0, 0])
    print s.largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247])


if __name__ == '__main__':
    main()
