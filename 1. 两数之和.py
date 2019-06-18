from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,num in enumerate(nums):
            exp_num = target - num
            if exp_num in nums:
                exp_idx = nums.index(exp_num)
                if idx != exp_idx:
                    return [ idx, exp_idx ]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,4,5],9))
