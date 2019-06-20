from typing import *

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return s in re.findall(p,s)
        
if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('aa','a'))
