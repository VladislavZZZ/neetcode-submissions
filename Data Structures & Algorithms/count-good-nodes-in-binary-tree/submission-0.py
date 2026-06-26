# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(cur: TreeNode, max_val: int ):
            if  not cur:
                return 0
            
            next_max = max(cur.val, max_val) 
            return int(cur.val>=max_val) + dfs(cur.left,next_max) + dfs(cur.right, next_max)
        
        return dfs(root, root.val)