from typing import *

n_min,n_max = -2147483648,2147483647

class Solution:
    def myAtoi(self, str: str) -> int:
        clean_str = str.strip()
        if not clean_str:return 0
        sign = ''
        if clean_str[0] in ('+','-'):
            sign = clean_str[0]
            clean_str = clean_str[1:]
        if not clean_str:return 0
        result_str = sign + clean_str[0]
        if not clean_str[0].isdigit():
            return 0
        for word in clean_str[1:]:
            if word.isdigit():
                result_str += word
            else:
                break
        result = int(result_str)
        result = min(result,n_max)
        result = max(result,n_min)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('  +3 21wwe'))
