from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 等需要学习链表时再说
# 此段代码只能在leetcode下通过
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        node = head
        while node:
            l.append(node.val)
            node = node.next
        l.pop(-n)
        return l

if __name__ == '__main__':
    s = Solution()
    # print(s.removeNthFromEnd([0,4,-5,2,-2,4,2,-1,4],4))
