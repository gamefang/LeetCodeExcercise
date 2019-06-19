from typing import *

n_min,n_max = -2147483648,2147483647

class Solution:
    def reverse(self, x: int) -> int:
        result = str(abs(x))[::-1]
        if x < 0:
            result = '-' + result
        result = int(result)        
        if n_min < result < n_max:
            return result
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(54532259954))
