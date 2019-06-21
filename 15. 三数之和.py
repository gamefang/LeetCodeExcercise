from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 超时……
        if len(nums) < 3: return []
        nums = sorted(nums) # 排序避免大部分麻烦
        result = []
        values = [None,None,None]
        for i in range(len(nums)):
            if len(nums) < 3 or nums[i] > 0: break  # 走到正数区间已经不可能匹配到了
            if nums[i] == values[0]: continue   # 重复的跳过，下同
            values[0] = nums[i]
            for j in range(len(nums)):
                if j == i: continue
                if nums[j] == values[1]: continue
                values[1] = nums[j]
                for k in range(len(nums)):
                    if k == j or k == i: continue
                    if nums[k] == values[2]: continue
                    values[2] = nums[k]
                    if nums[i] + nums[j] + nums[k] == 0:
                        triple = sorted([nums[i],nums[j],nums[k]])  # 排序避免大部分麻烦
                        if triple not in result:
                            result.append(triple)
                        break
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([2,0,1,-1,2,-2]))
