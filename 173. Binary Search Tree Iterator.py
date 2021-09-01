# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        # LC230
        # store most left nodes
        self.stack = []
        # root of subtree that possibly contains next node
        self.node = root
        # if self.node is None, next node is on top of stack

    def next(self) -> int:
        # add left most nodes of subtree
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        # pop the next node
        node = self.stack.pop()
        # right child is root of subtree that contains next node
        # if not None
        self.node = node.right
        return node.val

    def hasNext(self) -> bool:
        return self.stack or self.node

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
