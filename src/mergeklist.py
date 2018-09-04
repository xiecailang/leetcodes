#合并k个链表
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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        n = len(lists)
        while n > 1:
            k = int((n+1)/2)
            for i in range(0, int(n/2)):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+k])
            n = k
        return lists[0]

n1 = [int(i) for i in input().split()]
n2 = [int(i) for i in input().split()]
n3 = [int(i) for i in input().split()]

l1 = ListNode(0)
l2 = ListNode(0)
l3 = ListNode(0)

p1 = l1
p2 = l2
p3 = l3

for i in n1:
    t = ListNode(i)
    p1.next = t
    p1 = t

for i in n2:
    t = ListNode(i)
    p2.next = t
    p2 = t

for i in n3:
    t = ListNode(i)
    p3.next = t
    p3 = t

lists = [l1, l2, l3]
so = Solution()
ans = so.mergeKLists(lists)

p = ans
while p != None:
    print(p.val, end = '->')
    p = p.next