# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node, p, q):
        # return True if subtree rooted at node contains p or q
        if not node: return False

        inLeft = self.helper(node.left, p, q)
        inRight = self.helper(node.right, p, q)

        # assign LCA
        if inLeft and inRight:
            self.res = node
        elif (inLeft or inRight) and (node == p or node == q):
            self.res = node

        return inLeft or inRight or node == p or node == q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # note at the LCA node, either one of p and q is the LCA node
        # or p and q are in two subtrees

        self.res = None

        self.helper(root, p, q)

        return self.res
