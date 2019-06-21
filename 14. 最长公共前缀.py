from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        min_str = min(strs)
        max_str = max(strs)
        for idx,word in enumerate(min_str):
            if max_str[idx] != word:
                return min_str[:idx]
        return min_str

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["啊访问藕粉","啊我饿藕粉","啊我饿佛"]))
