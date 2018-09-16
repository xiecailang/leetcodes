#删除倒数第n个链表元素
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(-1)
        new_head.next = head
        p1 = new_head
        p2 = head
        for i in range(n+1):
            p2 = p2.next
        while p2 != None:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head