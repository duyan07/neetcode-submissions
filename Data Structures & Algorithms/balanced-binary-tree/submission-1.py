
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            
            l, r = dfs(node.left), dfs(node.right)
            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1
            return [balanced, max(l[1], r[1]) + 1]
        return dfs(root)[0]