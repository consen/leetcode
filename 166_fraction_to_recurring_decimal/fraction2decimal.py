# -*- coding: utf-8 -*-
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        ans = ''
        # 模拟正整数除法,所以负数先转成正数
        if numerator / denominator < 0:
            ans += '-'
            numerator = abs(numerator)
            denominator = abs(denominator)

        # 计算整数部分
        if numerator % denominator == 0:
            ans += str(numerator / denominator)
            return ans
        else:
            ans += str(numerator / denominator) + '.'
            numerator = numerator % denominator
        # 计算小数部分
        divisor = []
        while numerator != 0:
            # 除数重复则出现循环
            if numerator in divisor:
                pos = ans.find('.')
                ans = ans[0:pos+1+divisor.index(numerator)] + '(' + ans[pos+1+divisor.index(numerator):] + ')'
                break
            else:
                divisor.append(numerator)
            # 不足则除数进10
            numerator *= 10
            ans += str(numerator / denominator)
            numerator = numerator % denominator         # 余数作为新的除数
        return ans


def main():
    s = Solution()
    print s.fractionToDecimal(1, 2)
    print s.fractionToDecimal(2, 3)
    print s.fractionToDecimal(3, 2)
    print s.fractionToDecimal(1, 20)
    print s.fractionToDecimal(600, 2)
    print s.fractionToDecimal(601, 2)
    print s.fractionToDecimal(1, 99)
    print s.fractionToDecimal(1, 999)
    print s.fractionToDecimal(1, 17)
    print s.fractionToDecimal(1, 6)
    print s.fractionToDecimal(22, 7)
    print s.fractionToDecimal(-50, 8)
    print s.fractionToDecimal(-16, 8)
    print s.fractionToDecimal(7, 12)
    print s.fractionToDecimal(7, -12)


if __name__ == '__main__':
    main()
