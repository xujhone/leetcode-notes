# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        stack = []

        node = root

        while True:
            # add most left nodes to stack
            while node:
                stack.append(node)
                node = node.left
            # smallest element in the unvisited part
            node = stack.pop()
            k -= 1

            if not k:
                # if k == 0, it is the k-th node
                return node.val

            node = node.right

