# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        stack = [TreeNode(pre[0])]
        j = 0  # index on post

        # build tree in the order of preorder
        for v in pre[1:]:
            node = TreeNode(v)
            # find the parent of node
            while stack[-1].val == post[j]:
                # if stack[-1] == post
                # the subtree rooted at stack[-1] is created
                stack.pop()  # go up
                j += 1  # go to right sbling or root

            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node

            stack.append(node)

        return stack[0]
