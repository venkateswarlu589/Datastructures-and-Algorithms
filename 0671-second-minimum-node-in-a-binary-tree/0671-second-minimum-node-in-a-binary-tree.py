# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        min_ = 2**32
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != root.val:
                min_ = min(min_,node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return -1 if min_ == 2**32 else min_