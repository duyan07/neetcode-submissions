# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insertBST(node):
            if not node:
                return
            elif node.val < val and node.right is None:
                node.right = TreeNode(val)
                return
            elif node.val >= val and node.left is None:
                node.left = TreeNode(val)
                return
            
            if node.val < val:
                insertBST(node.right)
            else:
                insertBST(node.left)
        
        insertBST(root)
        return root if root else TreeNode(val)