class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        str = ''.join(re.findall('(^[\+\-]?\d*)', str))
        try:
            ret = int(str)
            if ret < -2147483648:
                return -2147483648
            elif ret > 2147483647:
                return 2147483647
            return ret
        except Exception:
            return 0