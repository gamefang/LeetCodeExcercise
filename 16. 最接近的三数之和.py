from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return None
        nums.sort() # 排序避免大部分麻烦
        result = float('inf')
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]: continue   # 重复的跳过
            p_left = i + 1
            p_right = len(nums) - 1
            while p_left < p_right:
                n_sum = nums[i] + nums[p_left] + nums[p_right]
                if n_sum == target:
                    return n_sum
                elif n_sum < target:
                    p_left += 1
                else:
                    p_right -= 1
                if abs(target - n_sum) < abs(target - result):
                    result = n_sum
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([2,0,1,-1,2,-2],33))
