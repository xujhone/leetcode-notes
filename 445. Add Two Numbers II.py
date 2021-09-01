# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def findLength(head):
            '''return length of linked list'''
            res = 0

            while head:
                res += 1
                head = head.next

            return res

        # find length of linked lists
        n1, n2 = findLength(l1), findLength(l2)

        cur1, cur2 = l1, l2
        cur = None

        while n1 > 0 or n2 > 0:
            val = 0
            # add corresponding nodes
            if n1 >= n2:
                val += cur1.val
                cur1 = cur1.next
                n1 -= 1
            if n1 < n2:
                val += cur2.val
                cur2 = cur2.next
                n2 -= 1

            cur = ListNode(val, cur)

        # cur points to the head
        # reverse the linked list and take care of carry
        carry = 0
        prev = None

        while cur:
            # update val for current node
            carry, cur.val = divmod(carry + cur.val, 10)
            # reverse pointers
            cur.next, cur, prev = prev, cur.next, cur

        # prev points to the head
        if carry:
            prev = ListNode(carry, prev)

        return prev
