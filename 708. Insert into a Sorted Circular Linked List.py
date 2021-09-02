"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        cur = head

        while True:
            # there are three cases:
            # 1) insertVal <= min
            # 2) min < insertVal < max
            # 3) insertVal >= max

            # for 2), add insertVal after current node when cur.val <= insertVal <= cur.next.val

            # for 1) and 3), add insertVal after max node
            # when cur.val > cur.next.val, current node is max node
            # when all nodes are equal, max = min, add insertVal to any position

            if cur.val <= insertVal <= cur.next.val or (
                    cur.val > cur.next.val and (insertVal <= cur.next.val or insertVal >= cur.val)):
                break

            cur = cur.next
            # if none of above happens after cur traverse all nodes
            # all elements are equal
            if cur == head:
                break

        cur.next = Node(insertVal, cur.next)

        return head
