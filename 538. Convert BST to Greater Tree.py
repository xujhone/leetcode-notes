# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        # given root of subtree
        # add each node by sum of nodes greater and inc
        # then return value of left most node, max of subtree
        def helper(node, inc):
            # if empty, inc is largest value
            if not node:
                return inc

            # if node has no children
            if node.left == node.right:
                node.val += inc
                return node.val

            # perform operations on right subtree first
            # update the node
            node.val += helper(node.right, inc)

            # change the inc to node.val
            return helper(node.left, node.val)

        helper(root, 0)

        return root
