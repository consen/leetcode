class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        l = len(nums)
        k = k % l
        nums[:] = list(reversed(list(reversed(nums[:l-k])) + list(reversed(nums[l-k:]))))

def main():
    s = Solution()
    n = [1, 2, 3, 4]
    s.rotate(n, 1)
    print(n)
    n = [1]
    s.rotate(n, 0)
    print(n)

if __name__ == '__main__':
    main()
