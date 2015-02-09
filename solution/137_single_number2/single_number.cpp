/*
class Solution:     # Wrong answer
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bit_count = [0] * 32
        for i in A:
            for j in range(0, 32):
                if (j >> i) & 1:
                    bit_count[j] += 1
        ans = 0
        for i in range(0, 32):
            ans |= (bit_count[i] % 3) << i
        return ans
*/

class Solution {
public:
    int singleNumber(int A[], int n) {
        int bit_count[32] = {0};
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < 32; j++) {
                if((A[i] >> j) & 1) {
                    bit_count[j]++;
                }
            }
        }
        int ans = 0;
        for(int i = 0; i < 32; i++) {
            ans |= (bit_count[i] % 3) << i;
        }
        return ans;
    }
};