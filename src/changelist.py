'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        ans = ListNode(0)
        ans.next = head
        pre = ans
        p1, p2 = head, head.next

        while p2 != None:
            pre.next = p2
            p1.next = p2.next
            p2.next = p1
            pre = p1
            p1 = p1.next
            if p1 == None:
                break
            p2 = p1.next
            
        return ans.next

n1 = [int(i) for i in input().split()]
l1 = ListNode(0)
p1 = l1
for i in n1:
    t = ListNode(i)
    p1.next = t
    p1 = t
l1 = l1.next

so = Solution()
l2 = so.swapPairs(l1)

p = l2
while p != None:
    print(p.val, end = '->')
    p = p.next