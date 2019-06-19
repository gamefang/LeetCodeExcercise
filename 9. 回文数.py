from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(-23522))
