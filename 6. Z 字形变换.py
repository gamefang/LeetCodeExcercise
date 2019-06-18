from typing import *

# 近似理解为古埃及木棒加密
# 1.准备空字符串矩阵：行=参数,列=len(串)
# 2.遍历字符串，按规律依次填入字符，类似走地图
#     起始点：r0c0
#     行进方向：下行，右上斜行
#     斜行条件：最底行 or (非最顶行 and 上方为空)
# 3.重新拼接字符串

class Solution:
    def convert(self, s: str, max_row: int) -> str:
        if max_row <= 1 or max_row >= len(s):return s
        max_col = len(s)
        matrix = [
            ['' for i in range(max_col)]
            for i in range(max_row)
        ]
        cur_row,cur_col = 0,0
        for word in s:
            matrix[cur_row][cur_col] = word
            if cur_row + 1 == max_row or \
               (cur_row != 0 and matrix[cur_row-1][cur_col] == ''):
                cur_row -= 1
                cur_col += 1
            else:
                cur_row += 1
        result = ''
        for row in matrix:
            result += ''.join(row)
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.convert('白日依山尽黄河入海流欲穷千里目更上一层楼',3))
