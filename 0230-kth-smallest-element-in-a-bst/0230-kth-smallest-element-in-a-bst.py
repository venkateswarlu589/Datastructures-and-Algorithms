# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        stack = []
        queue = collections.deque()
        queue.append(root)
        length = len(queue)
        while queue:
            list = []
            for i in range(length):
                node = queue.popleft()
                stack.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        stack.sort()
        return stack[k-1]
                    