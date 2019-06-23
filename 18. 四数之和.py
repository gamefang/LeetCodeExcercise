from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort() # 排序避免大部分麻烦
        result = []
        for p_start in range(len(nums)-3):
            if nums[p_start] + nums[p_start+1] + nums[p_start+2] + nums[p_start+3] > target: break  # 已经不可能匹配到了
            if p_start and nums[p_start] == nums[p_start-1]: continue   # 重复的跳过
            for p_end in range(3,len(nums))[::-1]:
                if nums[p_end] + nums[p_end-1] + nums[p_end-2] + nums[p_end-3] < target: break
                if p_end + 1 != len(nums) and nums[p_end] == nums[p_end+1]: continue
                p_left = p_start + 1
                p_right = p_end - 1
                while p_left < p_right:
                    n_sum = nums[p_start] + nums[p_left] + nums[p_right] + nums[p_end]
                    if n_sum == target:
                        result.append([ nums[p_start], nums[p_left], nums[p_right], nums[p_end] ])
                        p_left += 1
                        p_right -= 1
                        while p_left < p_right and nums[p_left] == nums[p_left-1]:
                            p_left += 1
                        while p_left < p_right and nums[p_right] == nums[p_right+1]:
                            p_right -= 1
                    elif n_sum > target:
                        p_right -= 1
                    else:
                        p_left += 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([0,4,-5,2,-2,4,2,-1,4],12))
