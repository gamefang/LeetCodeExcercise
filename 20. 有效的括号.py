from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        d_pair = {'(':')','[':']','{':'}'}
        rev_d_pair = {v:k for k,v in d_pair.items()}
        stack = []
        for word in s:
            if word in d_pair:
                stack.append(word)
            elif word in rev_d_pair:
                if stack and stack[-1] == rev_d_pair[word]:
                    stack.pop(-1)
                else:
                    return False
        return not stack

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('([]()()[][]'))
