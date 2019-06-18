from typing import *

# 毛毛虫的头每次往前蛄蛹一下。
# 如果头和身体有重复，就切掉重复的变成尾巴；
# 否则尾巴黏住不动身体变长。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slice_left = slice_right = result = 0
        while slice_right + 1 <= len(s) and len(s) - slice_left > result:
            slice_right += 1
            substr = s[slice_left:slice_right]
            if len(set(substr)) < len(substr):
                slice_left += substr.index(substr[-1]) + 1
            result = max(slice_right - slice_left,result)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
