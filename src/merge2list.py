#合并2个有序链表
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        p1 = l1
        p2 = l2
        h3 = ListNode(0)
        p3 = h3
        while p1 != None and p2 != None:
            t3 = ListNode(min(p1.val,p2.val))
            if p1.val <= p2.val:
                p1 = p1.next
            else:
                p2 = p2.next
            p3.next = t3
            p3 = p3.next
        if p1 == None and p2 != None:
            p3.next = p2
        elif p2 == None and p1 != None:
            p3.next = p1
        return h3.next

n1 = [int(i) for i in input().split()]
n2 = [int(i) for i in input().split()]

l1 = ListNode(0)
l2 = ListNode(0)

p1 = l1
p2 = l2

for i in n1:
    t = ListNode(i)
    p1.next = t
    p1 = t

for i in n2:
    t = ListNode(i)
    p2.next = t
    p2 = t

so = Solution()
l3 = so.mergeTwoLists(l1.next,l2.next)

p = l3
while p != None:
    print(p.val, end = '->')
    p = p.next

        