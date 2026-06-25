# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ancestor = root
        self.p, self.q, self.root = p,q, root
        def dfs(curr):
            if not curr:
                return [False, False]
            right, left = dfs(curr.right), dfs(curr.left)
            cur_state = [curr.val==self.p.val or right[0] or left[0], curr.val==self.q.val or right[1] or left[1]]
            if cur_state== [True,True] and self.ancestor == self.root:
                self.ancestor = curr
            return cur_state
        dfs(root)
        return self.ancestor