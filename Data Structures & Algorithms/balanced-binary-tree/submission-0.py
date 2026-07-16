
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def dfs(node):
            if not node: return 0

            l = dfs(node.left)
            r = dfs(node.right)
            if abs(l - r) > 1: 
                self.isBalanced = False
            return max(l, r) + 1

        dfs(root)
        return self.isBalanced