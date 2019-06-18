from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:return s
        result = s[0]
        for left_slice in range(len(s)-1):
            cur_s = s[left_slice:]
            if len(cur_s) <= len(result):break
            word_count = cur_s.count(cur_s[0])
            if word_count > 1:
                sub_s = cur_s
                for i in range(word_count-1):
                    right_slice = self._getFarestSameChar(sub_s)
                    cur_result = sub_s[:right_slice+1]
                    if len(cur_result) > len(result) and cur_result == cur_result[::-1]:
                        result = cur_result
                        break
                    else:
                        sub_s = sub_s[:right_slice]
        return result

    @staticmethod
    def _getFarestSameChar(s: str, char_idx: int = 0) -> int:
        return range(len(s))[::-1][s[::-1].index(s[char_idx])]


        # # 以下为最长头尾相等字符串
        # if not s:return s
        # max_len = 1
        # result = s[0]
        # used = set()
        # for idx,word in enumerate(s):
        #     if len(s[idx:]) <= max_len:break
        #     if word in used:continue
        #     if s.count(word) > 1:
        #         farest_idx = range(len(s))[::-1][s[::-1].index(word)]
        #         cur_len = farest_idx - idx + 1
        #         if cur_len > max_len:
        #             result = s[idx:farest_idx+1]
        #             max_len = cur_len
        #     used.add(word)
        # return result

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
