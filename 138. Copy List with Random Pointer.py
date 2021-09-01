"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        # need a map from ord to new

        # build the dict while copying

        # old, new in old2new
        # if old.random, new.random = old2new[old.random]

        old2new = {}

        old_curr = head

        new_prev = None

        while old_curr:
            # create the corresponding node for curr
            new_curr = old2new[old_curr] = Node(old_curr.val)

            # if not at the head
            if new_prev:
                new_prev.next = new_curr

            new_prev = new_curr
            old_curr = old_curr.next

        for old, new in old2new.items():
            try:
                new.random = old2new[old.random]
            except:
                pass

        return old2new[head]
