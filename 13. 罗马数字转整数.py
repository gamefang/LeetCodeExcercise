from typing import *

dic_int_roman = (
    (1000,'M'),
    (900,'CM'),
    (500,'D'),
    (400,'CD'),
    (100,'C'),
    (90,'XC'),
    (50,'L'),
    (40,'XL'),
    (10,'X'),
    (9,'IX'),
    (5,'V'),
    (4,'IV'),
    (1,'I'),
)

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for k_int,v_roman in dic_int_roman:
            while s.startswith(v_roman):
                s = s[len(v_roman):]
                result += k_int
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMLXXXVI'))
