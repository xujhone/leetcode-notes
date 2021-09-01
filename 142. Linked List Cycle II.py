# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # suppose there are n nodes: [0, 1, 2, ..., n-1]
        # suppose the node k in pointed by tail.next
        # when slow and fast first meet, fast traversed exactly number of nodes in the cycle than slow
        # thus, 2 * l - l = n - k, where l is the number of while loops
        # thus, slow and fast are at node n - k

        # note n - k + k = n - 1 + 1, thus after k more steps slow will be at the intersection

        slow = fast = head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle = True
                break

        if not cycle: return None

        while slow != head:
            slow = slow.next
            head = head.next

        return slow
