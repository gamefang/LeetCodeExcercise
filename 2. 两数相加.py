# 链表机制不明！

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 此段代码只能在leetcode下通过
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_num = Solution.ln_to_int(l1) + Solution.ln_to_int(l2)
        return [ int(num) for num in str(res_num)[::-1] ]

    @staticmethod
    def ln_to_int(ln):
        cur_str = ''
        cur_node = ln
        while 1:
            cur_str = str(cur_node.val) + cur_str
            cur_node = cur_node.next
            if cur_node is None:break
        return int(cur_str)

if __name__ == '__main__':
    s = Solution()
