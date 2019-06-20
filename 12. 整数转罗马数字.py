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
    def intToRoman(self, num: int) -> str:
        if num < 1 or num > 3999:return ''        
        result = ''
        for k_int,v_roman in dic_int_roman:
            result += v_roman * (num // k_int)
            num %= k_int
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(2019))
