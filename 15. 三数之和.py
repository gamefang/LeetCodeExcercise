from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort() # 排序避免大部分麻烦
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0: break  # 走到正数区间已经不可能匹配到了
            if i and nums[i] == nums[i-1]: continue   # 重复的跳过
            p_left = i + 1
            p_right = len(nums) - 1
            while p_left < p_right:
                n_sum = nums[i] + nums[p_left] + nums[p_right]
                if n_sum == 0:
                    result.append([ nums[i], nums[p_left], nums[p_right] ])
                    p_left += 1
                    p_right -= 1
                    while p_left < p_right and nums[p_left] == nums[p_left-1]:
                        p_left += 1
                    while p_left < p_right and nums[p_right] == nums[p_right+1]:
                        p_right -= 1
                elif n_sum > 0:
                    p_right -= 1
                else:
                    p_left += 1
        return result

        # # 超时……
        # if len(nums) < 3: return []
        # nums = sorted(nums) # 排序避免大部分麻烦
        # result = []
        # values = [None,None,None]
        # for i in range(len(nums)):
        #     if len(nums) < 3 or nums[i] > 0: break  # 走到正数区间已经不可能匹配到了
        #     if nums[i] == values[0]: continue   # 重复的跳过，下同
        #     values[0] = nums[i]
        #     for j in range(len(nums)):
        #         if j == i: continue
        #         if nums[j] == values[1]: continue
        #         values[1] = nums[j]
        #         for k in range(len(nums)):
        #             if k == j or k == i: continue
        #             if nums[k] == values[2]: continue
        #             values[2] = nums[k]
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triple = sorted([nums[i],nums[j],nums[k]])  # 排序避免大部分麻烦
        #                 if triple not in result:
        #                     result.append(triple)
        #                 break
        # return result

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([2,0,1,-1,2,-2]))
