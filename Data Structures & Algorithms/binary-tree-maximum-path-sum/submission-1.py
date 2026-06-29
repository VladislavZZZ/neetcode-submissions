# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(cur):
            if not cur:
                return 0

            leftMax , rightMax = max(dfs(cur.left),0), max(dfs(cur.right),0)
            self.res = max(self.res, cur.val + leftMax + rightMax)

            return cur.val + max(leftMax, rightMax)
        dfs(root)
        
        return self.res