#k个一组反转链表
'''
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def reverseOneGroup(self, pre, rear):
        last = pre.next
        cur = last.next
        while cur != rear:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last
            
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k <= 1:
            return head
        h = ListNode(0)
        h.next = head
        cur = head
        cnt = 0
        pre = h
        while cur != None:
            cnt += 1
            if cnt % k == 0:
                pre = self.reverseOneGroup(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next
        return h.next

n1 = [int(i) for i in input().split()]
k = int(input())
l1 = ListNode(0)
p1 = l1
for i in n1:
    t = ListNode(i)
    p1.next = t
    p1 = t
l1 = l1.next

so = Solution()
l2 = so.reverseKGroup(l1, k)

p = l2
while p != None:
    print(p.val, end = '->')
    p = p.next