# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True

        def dfs(curr1, curr2):
            if not curr1:
                self.isSame = not curr2
                return self.isSame

            self.isSame = True if (curr2 and curr1.val == curr2.val) else False
            if not self.isSame:
                return False
            left, right = dfs(curr1.left, curr2.left), dfs(curr1.right, curr2.right)
            return left and right
        
        return dfs(p, q)