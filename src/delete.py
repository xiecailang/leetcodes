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
        if n == 1 and head.next == None:
            return None
        p_end = head
        p_n = ListNode(-1)
        p_n.next = head
        cnt = 0
        len_ = 0
        while p_end != None:  
            len_ += 1          
            if cnt < n:
                cnt += 1
            else:
                p_n = p_n.next            
            p_end = p_end.next
        if len_ == n:
            head = head.next
        else:
            p_n.next = p_n.next.next
                           
        return head

nums = [int(i) for i in input().split()]
n = int(input())
head = ListNode(nums[0])
p = head
for i in range(1, len(nums)):
    temp = ListNode(nums[i])
    p.next = temp
    p = temp


sol = Solution()
head = sol.removeNthFromEnd(head, n)

p = head
while p != None:
    print('%d->' % p.val, end = '')
    p = p.next
print('None')
      
