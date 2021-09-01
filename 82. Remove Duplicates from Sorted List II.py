# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode(-101, head)
        # consider the new linked list starting at dummy head
        # since -100 <= node.val <= 100, dummy head should not be deleted

        # prev points to node that should not be deleted
        prev, cur = dummyHead, head
        # value of last deleted node
        duplicate = -101

        while cur and cur.next:
            if cur.val != duplicate and cur.val != cur.next.val:
                # current node should not be deleted
                prev = cur
            else:
                # cur.val == cur.next or cur.val == duplicate
                # delete current node
                duplicate = cur.val
                prev.next = cur.next

            cur = prev.next

        # either cur = None or cur.next = None
        if cur and cur.val == duplicate:
            # delete current node
            prev.next = cur.next

        return dummyHead.next
