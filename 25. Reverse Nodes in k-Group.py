# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        def helper(head):
            """
            Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
            """

            # count number of nodes in total
            total = 0
            tail = head
            while tail:
                total += 1
                if total == k:
                    break
                tail = tail.next

            # left-out nodes remain as it is
            if total < k:
                return head

            # tail points to the k-th node

            # reverse the rest nodes
            # return the head of the reversed linked list
            prev = helper(tail.next)
            cur = head
            # reverse the first k nodes
            while prev != tail:
                # swap pointers simultaneously
                cur.next, prev, cur = prev, cur, cur.next

            # prev points to the k-th node

            return prev

        return helper(head)
