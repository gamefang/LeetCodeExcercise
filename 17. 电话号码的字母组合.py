from typing import *

import itertools

btn_dic = {
    '0':' ',
    '1':'!@#',
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz',
    '*':'+',
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return [
            ''.join(item)
            for item in itertools.product(
                *[ btn_dic.get(i,'') for i in digits ]
            )
        ] if digits else []

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('357'))
