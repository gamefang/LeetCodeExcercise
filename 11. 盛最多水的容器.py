from typing import *

class Solution:
    def maxArea(self, y_points: List[int]) -> int:
        x_left,x_right = 0,len(y_points)-1
        result = 0
        while x_left < x_right:
            result = max( (x_right-x_left)*min(y_points[x_left],y_points[x_right]), result )
            if y_points[x_left] >= y_points[x_right]:
                x_right -= 1
            else:
                x_left += 1
        return result

        # 超时的暴力法
        # x_points = range(len(y_points))
        # d = dict( zip(x_points, y_points) )
        # result = 0
        # for cur_x in x_points:
        #     for exp_x in x_points[::-1]:
        #         if exp_x == cur_x:break
        #         result = max( min(d[exp_x], d[cur_x]) * (exp_x - cur_x), result )
        # return result

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
