# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # morris inorder traversal:

        curr = root

        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                # find its inorder predecessor
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right

                # prev points to inorder predecessor of curr

                # either prev.right == None
                if not prev.right:
                    # build a connection from prev to curr
                    prev.right = curr
                    curr = curr.left
                # or prev.right == curr
                else:
                    # already visited left subtree
                    # delete the connection
                    prev.right = None
                    res.append(curr.val)
                    curr = curr.right

        return res
