# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # use slow fast pointers to find first and second halves
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # either fast.next = None and number of nodes is odd
        # or fast.next.next = None and number of nodes is even
        # slow is at the end of first half

        # reverse the linked list starting at slow.next
        def reverseLinkedList(head, prev=None):
            curr = head

            while curr:
                curr.next, prev, curr = prev, curr, curr.next

            # curr = None and prev is the head of reversed linked list
            return prev

        tail = reverseLinkedList(slow.next, slow)

        left, right = head, tail

        while left != slow.next:
            if left.val != right.val:
                return False
            else:
                left, right = left.next, right.next

        # restore the second half linked list
        reverseLinkedList(tail)

        return True
