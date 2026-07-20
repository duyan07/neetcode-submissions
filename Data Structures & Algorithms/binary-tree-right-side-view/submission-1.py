# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if root:
            q.append(root)

        while q:
            right_side = None
            for i in range(len(q)):
                node = q.popleft()
                right_side = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if right_side:
                res.append(right_side)
        return res