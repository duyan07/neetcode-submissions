# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return None
            
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else: # root.val == key
            if not root.left and not root.right: # no children
                return None
            elif not root.right: # left child
                return root.left
            elif not root.left: # right child
                return root.right
            else: # both children
                minVal = self.minNode(root.right)
                root.val = minVal.val
                root.right = self.deleteNode(root.right, minVal.val)
        return root
